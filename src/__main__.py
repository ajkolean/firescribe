# main.py or app.py
from time import sleep

import logfire

from src.openai_service.openai_service import OpenAIService

logfire.configure()
service = OpenAIService()


# Your application logic
def main() -> None:
    logfire.info("Application has started.")
    print(service.fetch_assistantsList())
    while True:
        sleep(1)


if __name__ == "__main__":
    main()


#  def process_response_list(
#         self,
#         func: Callable[..., T],
#         *args: Any,
#         after = str | None = None,
#         **kwargs: Any,
#     ) -> list[T]:
#         all_items: list[T] = []

#         while True:
#             try:
#                 # Fetch a page of messages
#                 page: SyncCursorPage[T] = func(*args, **kwargs, after=after)

#                 if not page or not page.data:
#                     break  # No more messages to retrieve

#                 # Add the messages from the current page to the list
#                 all_items.extend(page.data)

#                 # Get the next page cursor (if available)
#                 a: PageInfo
#                 if next_page := page.next_page_info():
#                     parms = next_page.params
#                 else:
#                     break  # No more pages

#             except Exception as e:
#                 logfire.error(f"Error processing response list: {e}")
#                 return []

#         return all_items
