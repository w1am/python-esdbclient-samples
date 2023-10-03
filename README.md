## esdbclient Sample Code

This documentation provides sample code for [esdbclient](https://github.com/pyeventsourcing/esdbclient).

> **Note:** All issues related to this can be found on Linear.

I've prefixed certain comments with `#!` to distinguish between standard code comments and comments related to Linear issues.

Additionally, I've added region and endregion markers for VuePress.

### Prerequisites

1. [Poetry](https://python-poetry.org/docs/)
2. ESDB server running 

### Setting Up

1. **Install dependencies**:
    ```py
    poetry install
    ```

2. **Activate virtual environment**:
    ```py
    poetry shell
    ```

3. **Running the server**:
    ```bash
    docker-compose up
    ```

### Testing the Code

To experiment with the provided code snippets, use the `playground.py` file.