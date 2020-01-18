
ISS Tracker
===========


A. Correction to the Instructions
---------------------------------

Since the instructions were written, you now need to decode the value returned from "url.read()" before it can be used with "json.loads". So on page 2 of the instructions:

    result = json.loads(response.read())

needs to become:

    result = json.loads(response.read().decode('utf-8'))

Do not forget to add ".decode('utf-8')" wherever else "response.read()" is used in the instructions.



B. Additional Exercises
-----------------------

1. It takes 93 minutes for the ISS to complete an orbit around the world. Update the position of the ISS every 30 seconds for an hour, drawing a line between the previous and current position. You will need to take account of the sudden move from the right hand side of the map to the left to prevent a long straight line appearing across the map. 

2. Add in function definitions to remove duplicate code. Eg processing a URL