# Terminal Game: Bank Heist 

[Live Link](https://terminal-game.herokuapp.com/)

## What is Bank Heist?

Bank Heist is a text-based adventure game. Your character (randomised upon starting the game) is going to rob a bank. Every decision you make has consequences and you'll need to use logic to navigate safely through the security and open the bank vault to win.

## Planning process:

* In my initial design, I branched out the logic and paths a user could follow to either win the game or lose the game. The flow demonstrated when a user will make choices, face challenges and either win or lose.
![PP3 User Flow](https://user-images.githubusercontent.com/86608354/141331355-41acd957-9d4e-4ff6-9f34-f9ef0d3c26de.png)
* The original content for the game was drafted in a google doc to ensure spelling, punctuation and grammar were accurate. You can [view the google doc here](https://docs.google.com/document/d/1lgPP9bIV8M1vxFhaoXsuXvOUJz8m8mP5Ni0mhJJc1eQ/edit?usp=sharing)

### Changes to my planning process: 

* My original design path remains however it became apparent that the game could be navigated to completion very quickly. For this reason, I decided to add additional paths to each of the routes.
* As the design path changed additional content was required to furfill this.

## Technologies: 

For this project I will be using Python, HTML, CSS and some JavaScript.

### Frameworks, Libraries & Programs: 
* [GitPod](https://www.gitpod.io/) was the version control used.
* [GitHub](https://github.com/) is the repository used for project codes to be pushed from GitPod.
* [Flowmap](https://www.flowmapp.com) was used to create user flowmaps during the design process of this project.
* [Heroku](https://www.heroku.com/) was used to deplpoy the game to a live cloud based applicaiton.

## Features 

### Current features:

* F1 - Loading the game 

The game can be loaded via [this link](https://terminal-game.herokuapp.com/). After opening the game you will be greeted with this statement.

* F2 - Character generator 

Everytime you start the game your character is automatically generated. Three unique selections are made from an array to give the user a unique experience everytime they play. The user has 140 total combinations possible when starting the game. See some examples below.

<img width="766" alt="Screenshot 2021-11-16 at 11 46 30" src="https://user-images.githubusercontent.com/86608354/141980343-7d2ca231-e546-4315-96bf-882738c7656d.png">
<img width="766" alt="Screenshot 2021-11-16 at 11 46 38" src="https://user-images.githubusercontent.com/86608354/141980349-9b7b57ed-8c64-432c-b6b4-845beb3cf145.png">
<img width="766" alt="Screenshot 2021-11-16 at 11 46 23" src="https://user-images.githubusercontent.com/86608354/141980359-37e51122-5962-43ac-9997-bac896f46bbd.png">

* F3 - Starting the game 

After recieving your character, the user will need to press enter to start the game.

<img width="761" alt="Screenshot 2021-11-16 at 11 53 18" src="https://user-images.githubusercontent.com/86608354/141980748-5ac772fb-ff4d-4ca5-8f93-fd0bb168d9c1.png">

* F4 - First decision 

The first decision allows the user to pick which unique route they would like to use. This gives the game repeatability as a user can play again and again to keep trying alternative routes.

<img width="761" alt="Screenshot 2021-11-16 at 11 53 56" src="https://user-images.githubusercontent.com/86608354/141980835-d2f4125b-f094-4082-9368-786ff01e808f.png">


* F5 - Random number generator 

This challenge requires the user to input a number between 1 and 5 into the terminal. If that number is equal to the number randonmly generated then they will proceed otherwise they will lose the game. 

<img width="738" alt="Screenshot 2021-11-16 at 11 55 02" src="https://user-images.githubusercontent.com/86608354/141981038-f974dca2-9610-4a85-8f85-c932287adef6.png">
<img width="738" alt="Screenshot 2021-11-16 at 11 55 12" src="https://user-images.githubusercontent.com/86608354/141981047-5452338a-3ee7-4afc-8f33-02e8d4ae6cff.png">
<img width="738" alt="Screenshot 2021-11-16 at 11 55 23" src="https://user-images.githubusercontent.com/86608354/141981053-8e73ea5a-e389-44ab-8683-6ab731bf9108.png">


* F6 - Keypad loop puzzle 

The user is presented with three numbers which make up a three number combination. This while loop allows the user to keep guessing what the correct combination is and will allow the user to pass when answered correctly.

<img width="738" alt="Screenshot 2021-11-16 at 11 56 40" src="https://user-images.githubusercontent.com/86608354/141981294-d31e0130-2265-444e-8771-afedc192d68f.png">
<img width="738" alt="Screenshot 2021-11-16 at 11 56 48" src="https://user-images.githubusercontent.com/86608354/141981302-ba4462b9-24bb-464b-919f-e026eea92390.png">
<img width="738" alt="Screenshot 2021-11-16 at 11 57 03" src="https://user-images.githubusercontent.com/86608354/141981309-3fd97497-6bef-4f79-b780-49262efa6f5d.png">


* F7 - Word input 

User will need to input a word to proceed on the route.

![Screenshot 2021-11-16 at 14 58 00](https://user-images.githubusercontent.com/86608354/142009384-fdc90d23-bda8-453e-a6b1-439469f1c252.png)

* F8 - 1st Maths Puzzle 

The user will be presented with a puzzle which requires some logically thinking. If the user gets the puzzle correct they will proceed otherwise they will lose the game.

![Screenshot 2021-11-16 at 14 58 18](https://user-images.githubusercontent.com/86608354/142009408-5a20b973-90a0-4251-a355-97e5b8545560.png)
![Screenshot 2021-11-16 at 14 59 40](https://user-images.githubusercontent.com/86608354/142009488-131b4baa-9139-42ae-a5e3-388e84fda689.png)
![Screenshot 2021-11-16 at 14 58 29](https://user-images.githubusercontent.com/86608354/142009514-cec028bd-a82d-4867-9e7d-dc9d981ff02e.png)

* F9 - 2nd Maths Puzzle 

Similar to the first maths puzzle however this is more of a riddle than puzzle. The user will need to get it right first time to proceed and win.

![Screenshot 2021-11-16 at 14 58 43](https://user-images.githubusercontent.com/86608354/142009544-7df08c5e-0ead-446e-8723-3d3217b5ea09.png)
![Screenshot 2021-11-16 at 14 59 24](https://user-images.githubusercontent.com/86608354/142009574-58182928-7756-4bf9-be9b-716c61a46931.png)

* F10 - Key date puzzle 

The user will need to read and comprehend the content provided to ensure they know the password to proceed with the game. They will only get one attempt to get this right otherwise the game is over.
![Screenshot 2021-11-16 at 15 01 52](https://user-images.githubusercontent.com/86608354/142010138-e947e6cc-84e9-4e1a-aaef-fbf0075693cc.png)
![Screenshot 2021-11-16 at 15 02 05](https://user-images.githubusercontent.com/86608354/142010191-c2b71f39-cabc-4900-b2a5-d76bc6ab534d.png)
![Screenshot 2021-11-16 at 15 02 19](https://user-images.githubusercontent.com/86608354/142010217-b32a5eb6-3db9-4541-870c-c01db3b31651.png)


### Features which could be implemented in the future:

* F11 - Easter Egg

With additional time I would like to add an Easter Egg to the game. Many game players enjoy searching and hunting for easter eggs so I feel this addition would improve the value and playability of my game.

* F12 - User Login

I'd like to add the availbility for a user to create an account for the game. This would require a user to register a username and password which will then be stored in a google sheet and linked via an API. With this added, it would give the game scope to enhance the user experience and furthering the way users interact with the game.

## Testing 

Testing was undertaken at the start, during and after finishing my project. To complete my testing I used the [Google Chrome DevTool](https://developer.chrome.com/docs/devtools/), a spreadsheet to track tests, validators (as seen below) and reviews by peers (as seen in the credits).

### Feature testing 
* Each feature was tested. If the feature responded correctly then it was marked green on my spreadsheet.
* All of the features were compared against the original idea and I ensured they met the crtieria I set out with. 

### Validator testing 

* HTML 
  * Testing results below [W3C validator](https://validator.w3.org/nu/#textarea) 
  
<img width="1277" alt="Screenshot 2021-11-16 at 12 18 27" src="https://user-images.githubusercontent.com/86608354/141984130-bdf54d2d-f66e-4690-88a4-9880d64bec01.png">
<img width="1277" alt="Screenshot 2021-11-16 at 12 19 07" src="https://user-images.githubusercontent.com/86608354/141984157-f5f1897b-0d0d-4879-97c2-8886575c788d.png">

* PEP8 
 * No major errors were found when passing through the [PEP8 Online Check] (http://pep8online.com/checkresult)
 
  <img width="1277" alt="Screenshot 2021-11-16 at 12 15 59" src="https://user-images.githubusercontent.com/86608354/141983814-a7c3f949-e508-42fa-a72d-8f89bba7c6d0.png">

 ### Known Bugs 
 
 * After deploying to Heroku, I noticed that some text would be cut off by the terminal as seen below.
  
 <img width="766" alt="Screenshot 2021-11-16 at 11 40 33" src="https://user-images.githubusercontent.com/86608354/141979987-2a36db64-4789-4eb5-91ce-0f63da40b614.png">
 
 * I implemented a fix to this bug which now ensures the introduction text fits correctly on the terminal.
 
<img width="766" alt="Screenshot 2021-11-16 at 11 46 23" src="https://user-images.githubusercontent.com/86608354/141980068-1da07aa5-17d6-4a76-a5a1-04022ff9777e.png">

* During my testing I noticed that the terminal clearing was not working as intended - see screenshot below.

<img width="761" alt="FIX THIS" src="https://user-images.githubusercontent.com/86608354/141984716-c0c0d235-4974-4276-972f-0867284de50e.png">

* I implemented a fix to this bug which now ensures the terminal clears correctly.

![Screenshot 2021-11-16 at 15 37 33](https://user-images.githubusercontent.com/86608354/142016535-9dd73a25-a417-45d9-a259-45de13b7ef9c.png)
![Screenshot 2021-11-16 at 15 39 33](https://user-images.githubusercontent.com/86608354/142016624-cb56157c-0fe3-4cd7-887d-c60b7ee0e6dc.png)
 
 ## Deployment via Heroku 
 
 [Live Link](https://terminal-game.herokuapp.com/)

### How was this site deployed? 

To deploy the site I used [Heroku](https://www.heroku.com/) a Cloud Application Platform. 

* To start, I named my app and created the profile.

<img width="1664" alt="Screenshot 2021-11-15 at 16 02 32" src="https://user-images.githubusercontent.com/86608354/141974595-cb54c170-3579-4be1-b27c-5f128bac6e64.png">

* Next I set my Config Vars to ensure that the app would deploy as anticipated.

<img width="1658" alt="Screenshot 2021-11-15 at 16 02 46" src="https://user-images.githubusercontent.com/86608354/141974692-7c83f672-d466-4fdf-8d13-85d2d8cc76d8.png">

* Following the Config Vars, I added the correct buildpacks in order. For this project, only the Python and nodeJS were required.

<img width="1658" alt="Screenshot 2021-11-15 at 16 02 58" src="https://user-images.githubusercontent.com/86608354/141974866-84322abc-ac79-4522-8104-1f734b01dfae.png">

* To connect with my repository, I needed to connect my GitHub. 

<img width="1658" alt="Screenshot 2021-11-15 at 16 03 19" src="https://user-images.githubusercontent.com/86608354/141974947-89e0d43c-2214-4871-b68c-325e74b3bce9.png">

* After connecting to my GitHub, I could link the repository.

<img width="1658" alt="Screenshot 2021-11-15 at 16 03 26" src="https://user-images.githubusercontent.com/86608354/141975018-b1857711-0052-4e5c-a6a7-9665eb87420f.png">

* Then I needed to select the branch to deploy from.

<img width="1658" alt="Screenshot 2021-11-15 at 16 03 36" src="https://user-images.githubusercontent.com/86608354/141975136-4505380e-cd17-45b5-a122-11c7fedc810d.png">

* Lastly, I deployed the project succesfully.

<img width="1658" alt="Screenshot 2021-11-15 at 16 04 48" src="https://user-images.githubusercontent.com/86608354/141975195-52de0793-aad8-46ea-9524-39636f0d9847.png">


 ## Credits:
 
 * To ensure my CSS code was formatted correctly, I ran it through a formatter which can be found here: [CSS Code Formatter](https://www.freeformatter.com/css-beautifier.html#ad-output)
 * To ensure my HTML code was formatted correctly, I ran it through a formatter which can be found here: [HTML Code Formatter](https://www.freeformatter.com/html-formatter.html)
 * To ensure my JavaScript code was formatted correctly, I ran it through a formatter which can be found here: [JavaScript Code Formatter](https://beautifier.io/)
 * To ensure my Python code was formatted correctly, I ran it through a PEP8 formatter which can be found here: [Python Formatter](https://codebeautify.org/python-formatter-beautifier) 

### Content 

* For interesting maths puzzles I used [CUE MATH](https://www.cuemath.com/learn/fun-maths-questions/) and selected a few of their puzzles for my game. They were slightly adjusted to suit my theme.

### Code 

* As a go to reasource hub I used [W3S Schools](https://www.w3schools.com/default.asp).
* To create my responsive picture examples I used [ami.responsive](http://ami.responsivedesign.is).
* When stuck on a development issue, I checked [Stackoverflow](https://stackoverflow.com) to see if other developers had the same problems.

### Acknowledgments 

* I'd like to thank Brian Macharia for providing feedback, ideas and suggestions to improve my project.
