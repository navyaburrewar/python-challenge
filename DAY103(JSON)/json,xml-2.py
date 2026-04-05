#  JSON vs XML
# When it comes to data formats, JSON and XML are the two most common choices. JSON is generally preferred for web applications due to its smaller size, ease of use, and better performance. Here's a quick comparison:


# Feature	                 JSON	                                  XML
# Readability     	Human-readable	                        Human-readable but more verbose
# Data Size	       Smaller and more compact	               Larger due to extra markup
# Parsing	           Easier to parse in most languages	       More complex parsing
# Support         	Broad support across languages	       Initially JavaScript, but now widely supported
# Use Cases	        Web APIs, configuration files,          data transfer	Data storage, document formatting




# How JSON Data Flow Works in Web Applications
# In a typical web application, JSON (JavaScript Object Notation) is used to transfer data between the server and the client (frontend). JSON is language-independent, which makes it ideal for communication between different technologies.


# Server Side
# Server Side
# Data is stored as an object (for example, a dictionary or class instance).
# Before sending the data over the network, it is converted into a JSON string.
# This JSON string is sent to the client through an API response (such as an HTTP GET request).

# Client Side
# The client receives the data as a JSON string.
# The JSON string is parsed back into a native object depending on the programming language used.
# Once parsed, individual values can be accessed and used in the application.
# Example JSON String Received from Server

# {"name":"Mohit", "age":30}


# This JSON data contains:

# name: "Mohit"
# age: 30