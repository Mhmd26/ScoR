import asyncio
import functools
import shlex
from typing import Tuple
from telethon import functions, types
from ...core.logger import logging

LOGS = logging.getLogger(__name__)

# Function to execute terminal commands asynchronously
async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """Execute a terminal command asynchronously and return the output."""
    try:
        # Split the command into arguments using shlex
        args = shlex.split(cmd)
        
        # Create a subprocess to execute the command
        process = await asyncio.create_subprocess_exec(
            *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        
        # Wait for the process to complete and capture stdout and stderr
        stdout, stderr = await process.communicate()
        
        # Return the decoded output, error output, return code, and process ID
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )
    except Exception as e:
        LOGS.error(f"Error running command: {cmd} | {e}")
        return "", str(e), 1, 0

# Function to run synchronous code asynchronously
def run_sync(func, *args, **kwargs):
    """Run a function synchronously in a separate thread."""
    return asyncio.get_event_loop().run_in_executor(
        None, functools.partial(func, *args, **kwargs)
    )

# Function to run an asynchronous function with a specific event loop
def run_async(loop, coro):
    """Run an async function in a specific loop."""
    return asyncio.run_coroutine_threadsafe(coro, loop).result()

# Function to run async functions directly
def runasync(func: callable):
    """Run async functions with the right event loop."""
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(func)

# Function to unsave a gif using Telethon's API
async def unsavegif(event, jasme):
    """Unsave a gif document using Telethon."""
    try:
        # Make the SaveGifRequest call to unsave the gif
        await event.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=jasme.media.document.id,
                    access_hash=jasme.media.document.access_hash,
                    file_reference=jasme.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        # Log any exceptions that occur during the process
        LOGS.info(f"Error unsaving gif: {str(e)}")
