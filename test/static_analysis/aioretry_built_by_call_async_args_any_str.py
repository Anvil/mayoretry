'''Test aioretry_built_by_call_async_args_any_str.py '''

# flake8: noqa
# pylint: disable=unused-import, unused-argument, invalid-name, R0801


import asyncio
from typing import Any
from collections.abc import Callable, Awaitable
from mypy_extensions import VarArg, KwArg
from kaioretry import retry, aioretry, Retry, Context


async def func(*args: Any) -> str:
    ''' ... '''
    return 'return_value'


wrapped: Callable[[VarArg(Any)], Awaitable[str]] = Retry(exceptions=(ValueError, NotImplementedError), context=Context(tries=5, delay=2)).aioretry(func)


async def use_decoration(parameter: str) -> str:
    ''' obtain result and use it '''
    result = await wrapped(1, 2)
    assert isinstance(result, str)
    return f"parameter is {parameter}. result is {result}"


if __name__ == "__main__":
    print(asyncio.run(use_decoration("value")))
