#!/usr/bin/env python3
# ex: set filetype=python:

"""Translate an XDR specification into executable code that
can be compiled for the Linux kernel."""

import logging

from argparse import Namespace
from lark import logger
from lark.exceptions import VisitError

from OS.linux.tools.net.sunrpc.xdrgen.generators.constant import XdrConstantGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.enum import XdrEnumGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.header_bottom import XdrHeaderBottomGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.header_top import XdrHeaderTopGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.passthru import XdrPassthruGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.pointer import XdrPointerGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.program import XdrProgramGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.typedef import XdrTypedefGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.struct import XdrStructGenerator
from OS.linux.tools.net.sunrpc.xdrgen.generators.union import XdrUnionGenerator

from OS.linux.tools.net.sunrpc.xdrgen.xdr_ast import transform_parse_tree, Specification
from OS.linux.tools.net.sunrpc.xdrgen.xdr_ast import _RpcProgram, _XdrConstant, _XdrEnum, _XdrPassthru, _XdrPointer
from OS.linux.tools.net.sunrpc.xdrgen.xdr_ast import _XdrTypedef, _XdrStruct, _XdrUnion
from OS.linux.tools.net.sunrpc.xdrgen.xdr_parse import xdr_parser, set_xdr_annotate
from OS.linux.tools.net.sunrpc.xdrgen.xdr_parse import make_error_handler, XdrParseError
from OS.linux.tools.net.sunrpc.xdrgen.xdr_parse import handle_transform_error

logger.setLevel(logging.INFO)


def emit_header_definitions(root: Specification, language: str, peer: str) -> None:
    """Emit header definitions"""
    for definition in root.definitions:
        if isinstance(definition.value, _XdrConstant):
            gen = XdrConstantGenerator(language, peer)
        elif isinstance(definition.value, _XdrEnum):
            gen = XdrEnumGenerator(language, peer)
        elif isinstance(definition.value, _XdrPointer):
            gen = XdrPointerGenerator(language, peer)
        elif isinstance(definition.value, _RpcProgram):
            gen = XdrProgramGenerator(language, peer)
        elif isinstance(definition.value, _XdrTypedef):
            gen = XdrTypedefGenerator(language, peer)
        elif isinstance(definition.value, _XdrStruct):
            gen = XdrStructGenerator(language, peer)
        elif isinstance(definition.value, _XdrUnion):
            gen = XdrUnionGenerator(language, peer)
        elif isinstance(definition.value, _XdrPassthru):
            gen = XdrPassthruGenerator(language, peer)
        else:
            continue
        gen.emit_definition(definition.value)


def emit_header_maxsize(root: Specification, language: str, peer: str) -> None:
    """Emit header maxsize macros"""
    print("")
    for definition in root.definitions:
        if isinstance(definition.value, _XdrEnum):
            gen = XdrEnumGenerator(language, peer)
        elif isinstance(definition.value, _XdrPointer):
            gen = XdrPointerGenerator(language, peer)
        elif isinstance(definition.value, _XdrTypedef):
            gen = XdrTypedefGenerator(language, peer)
        elif isinstance(definition.value, _XdrStruct):
            gen = XdrStructGenerator(language, peer)
        elif isinstance(definition.value, _XdrUnion):
            gen = XdrUnionGenerator(language, peer)
        elif isinstance(definition.value, _RpcProgram):
            gen = XdrProgramGenerator(language, peer)
        else:
            continue
        gen.emit_maxsize(definition.value)


def subcmd(args: Namespace) -> int:
    """Generate definitions"""

    set_xdr_annotate(args.annotate)
    parser = xdr_parser()
    with open(args.filename, encoding="utf-8") as f:
        source = f.read()
        try:
            parse_tree = parser.parse(
                source, on_error=make_error_handler(source, args.filename)
            )
        except XdrParseError:
            return 1
        try:
            ast = transform_parse_tree(parse_tree)
        except VisitError as e:
            handle_transform_error(e, source, args.filename)
            return 1

        gen = XdrHeaderTopGenerator(args.language, args.peer)
        gen.emit_definition(args.filename, ast)

        emit_header_definitions(ast, args.language, args.peer)
        emit_header_maxsize(ast, args.language, args.peer)

        gen = XdrHeaderBottomGenerator(args.language, args.peer)
        gen.emit_definition(args.filename, ast)

    return 0
