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

Everytime you start the game your character is automatically generated. Three unique selections are made from an array to give the user a unique experience everytime they play.

* F3 - Starting the game 

After recieving your character, the user will need to press enter to start the game.

* F4 - First decision 

The first decision allows the user to pick which unique route they would like to use. This gives the game repeatability as a user can play again and again to keep trying alternative routes.

* F5 - Random number generator 

This challenge requires the user to input a number between 1 and 5 into the terminal. If that number is equal to the number randonmly generated then they will proceed otherwise they will lose the game. 

* F6 - Keypad loop puzzle 

The user is presented with three numbers which make up a three number combination. This while loop allows the user to keep guessing what the correct combination is and will allow the user to pass when answered correctly.

* F7 - Word input 

User will need to input a word to proceed on the route.

* F8 - 1st Maths Puzzle 

The user will be presented with a puzzle which requires some logically thinking. If the user gets the puzzle correct they will proceed otherwise they will lose the game.

* F9 - 2nd Maths Puzzle 

Similar to the first maths puzzle however this is more of a riddle than puzzle. The user will need to get it right first time to proceed and win.

* F10 - Key date puzzle 

The user will need to read and comprehend the content provided to ensure they know the password to proceed with the game. They will only get one attempt to get this right otherwise the game is over.

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
  * Testing results below [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html) 
  
 * CSS
   * No erros were found when passing through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/)  
   
 * JavaScript

* PEP8 
 * No major errors were found when passing through the [PEP8 Online Check] (http://pep8online.com)

 ### Accessibility testing 


 ### Known Bugs 
 
 * 
 
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
 * To ensure my Python code was formatted correctly, I ran it through a PEP8 formatter which can be found here: 

### Content 

* For interesting maths puzzles I used [CUE MATH](https://www.cuemath.com/learn/fun-maths-questions/) and selected a few of their puzzles for my game. They were slightly adjusted to suit my theme.

### Code 

* As a go to reasource hub I used [W3S Schools](https://www.w3schools.com/default.asp).
* To create my responsive picture examples I used [ami.responsive](http://ami.responsivedesign.is).
* When stuck on a development issue, I checked [Stackoverflow](https://stackoverflow.com) to see if other developers had the same problems.

### Acknowledgments 

* I'd like to thank Brian Macharia for providing feedback, ideas and suggestions to improve my project.
