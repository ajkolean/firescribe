from multiprocessing import process
from typing import Any, Callable, Dict, List, Literal, Optional, TypeVar

import logfire
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from openai.pagination import PageInfo, SyncCursorPage
from openai.types.beta import Assistant

from src.utils.settings import settings

T = TypeVar("T")


# Logfire configuration
load_dotenv()


class OpenAIService:
    def __init__(self):
        settings.model_dump()
        # Initialize OpenAI client
        self.client = OpenAI()
        print("OpenAI client initialized.")
        # logfire.info("OpenAI client initialized.")

    def fetch_assistantsList(self) -> list[Assistant]:
        """Fetches a list of all assistants."""
        return self.process_response_list(
            self.client.beta.assistants.list, after=None
        )

    def process_response_list(
        self,
        func: Callable[..., T],
        *args: Any,
        after: str | None = None,
        **kwargs: Any,
    ) -> list[T]:
        all_items: list[T] = []
        print("process_response_list")
        while True:
            try:
                # Fetch a page of messages
                page: SyncCursorPage[T] = func(*args, **kwargs, after=after)

                if not page or not page.data:
                    print(page)
                    break  # No more messages to retrieve

                # Add the messages from the current page to the list
                all_items.extend(page.data)

                # Get the next page cursor (if available)
                if next_page := page.next_page_info():
                    after = (
                        next_page.params.get("after")
                        if isinstance(next_page.params.get("after"), str)
                        else None
                    )
                    print(after)
                else:
                    break  # No more pages

            except Exception as e:
                logfire.error(f"Error processing response list: {e}")
                break

        return all_items


o = OpenAIService()
print(o.fetch_assistantsList())
