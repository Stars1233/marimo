# Copyright 2024 Marimo. All rights reserved.
from __future__ import annotations

from marimo._cli.envinfo import (
    get_system_info,
)


def test_get_node_version() -> None:
    system_info = get_system_info()
    assert "Binaries" in system_info
    assert "Node" in system_info["Binaries"]
    node_version = system_info["Binaries"]["Node"]

    assert node_version is None or isinstance(node_version, str)


def test_get_package_versions() -> None:
    system_info = get_system_info()
    assert "Dependencies" in system_info
    package_versions = system_info["Dependencies"]

    assert isinstance(package_versions, dict)
    assert "click" in package_versions
    assert "starlette" in package_versions
    assert "pymdown-extensions" in package_versions
    assert package_versions["pymdown-extensions"] != "missing"


def test_get_system_info() -> None:
    system_info = get_system_info()
    assert isinstance(system_info, dict)
    assert "marimo" in system_info
    assert "OS" in system_info
    assert "OS Version" in system_info
    assert "Python Version" in system_info
    assert "Binaries" in system_info
    assert "Dependencies" in system_info
    assert "Experimental Flags" in system_info
