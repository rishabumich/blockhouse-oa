# Blockhouse Takehome Project

#### By Rishab Gupta

Thank you for taking the time to review my project! :)

## Steps for Usage

- cd into server directory and run 'pip install' to make sure all dependencies are in your local project
- cd into the client directory and run 'npm install' to make sure all next dependencies are in your local project
- In the server, run 'python3 manage.py runserver' to allow the server port to open
- In the client, run 'npm run dev' to put the frontend in development mode
- Navigate to 'localhost:3000' and the Next app should be successfully running!

For the backend, I set up API routes with very clear identifiers and then used axios on the frontend to query these APIs and get their data. I split up the front-end into various reusable components which would query the data from a specified API point. This is great because I can now add a new route with different data and just by changing the endpoint, I can have a new chart with new data; much better than constantly code duplicating.

I used Typescript in this project which ensured all my types were unassumed and no implicit casting was happening! I used a lot of the skills I had from past projects but learned a TON through this project with ChartJS specifically and new tools I hadn't worked with before. This project showcases my skills from previous internships using these tools as well as my skills in learing on the fly and using external tools to implement unfimailiar code.
