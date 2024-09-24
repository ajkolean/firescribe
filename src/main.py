# main.py or app.py
import logfire

logfire.configure()


# Your application logic
def main() -> None:
    logfire.info("Application has started.")


if __name__ == "__main__":
    main()
