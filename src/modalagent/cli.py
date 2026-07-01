"""Command-line entry point for ModalAgent."""

import logging
import os

from modalagent.server import main as server_main

logger = logging.getLogger("ModalAgent")


def main() -> None:
    log_level = os.getenv("MODAL_LOG_LEVEL", "INFO")
    logging.basicConfig(level=getattr(logging, log_level.upper(), logging.INFO))
    logger.info("Starting ModalAgent")
    server_main(log_level=log_level)


if __name__ == "__main__":
    main()
