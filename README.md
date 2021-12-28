<h1 align="center">API</h1>

This API is an internal service that serves as an abstraction layer between my persistent storage and my client-facing infrastructure such as my website.
The API is currently publicly accessible although this is subject to
change in future circumstances.

Being tightly coupled with the functionality being provided by my other infrastructure, 
this API will not be strictly versioned and does
not provide any guaranteed behaviour at any point in time.

## Project information

This API uses the GraphQL format demonstrated by Facebook. The main structure is in Python
using the FastAPI and Strawberry 🍓 libraries for the interface and SQLModel for interacting
with the database.
