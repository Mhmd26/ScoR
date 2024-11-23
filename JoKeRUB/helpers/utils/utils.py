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
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
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
        # Check if jasme and its attributes are valid
        if not hasattr(jasme, 'media') or not hasattr(jasme.media, 'document'):
            LOGS.error("Invalid 'jasme' object or missing 'media' or 'document'.")
            return
        
        document = jasme.media.document
        if not document:
            LOGS.error("Document is missing in the provided 'jasme' object.")
            return
        
        # Log document details for debugging purposes
        LOGS.info(f"Attempting to unsave GIF with ID: {document.id} and Access Hash: {document.access_hash}")
        
        # Execute the SaveGifRequest to unsave the gif
        await event.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=document.id,
                    access_hash=document.access_hash,
                    file_reference=document.file_reference,
                ),
                unsave=True,
            )
        )
        LOGS.info("Successfully unsaved the GIF.")
    except Exception as e:
        # Log any exceptions that occur during the process
        LOGS.error(f"Error unsaving gif: {str(e)}")
