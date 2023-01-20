# OVERVIEW

This template was made as a guide to ensure you cover assessment criteria in your third milestone write up. It is specific to the **PORTFOLIO 3: Python Essentials** project. It was based off the [battleship readme](https://codeinstitute.s3.amazonaws.com/CSSEssentials/p3-readme.png) with a few additions to help elevate you to possible distinction status.


Sections marked as 🚨**Required**  and 🚀 **merit & beyond**

**Please note** that project assessment criteria changes more often than these guides are updated so double-check the submission criteria before assuming the  🚨**Required**  is all you have to do to pass.

## Helpful tools

### Debugging Your run.py in gitpod
With a single file importing others, gitpod lets you set breakpoints where you then can look at variables and try out syntax.

https://user-images.githubusercontent.com/23039742/212526268-ec02736e-e199-4c63-92b0-96b219f24abc.mp4


### Screenshots and Videos
**Here’s a great video on how to add videos to your readme! no need to convert to gifs!!**

https://www.youtube.com/watch?v=G3Cytlicv8Y

> 1. record a video via slack
> 2. download it
> 3. in github, edit your readme via the pencil icon
> 4. type a place holder word and highlight it
> 5. drag and drop mp4 file over that text
> 6. scroll down to the commit area
> 7. update the default commit message
> 8. click the green button
> 9. ```git pull``` changes to your gitpod workspace

**You can do the steps 3-9 for the image/screenshot uploads too!**

### Cheatsheets and Auto Generation Tools

Markdown's not all that easy so sometimes you may want to use some tools to make tables. 

- [Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
- [markdown table generator](https://www.tablesgenerator.com/markdown_tables) - used to help with documentation table formatting
- [mardown table of contents generator](https://luciopaiva.com/markdown-toc/) - used to create table of contents (be weary it does have some bugs if you have dashes or trailing spaces in your headers)
- [readme.so](https://readme.so/) - if you don't want to learn markdown, this tool might help you

# Table of Contents
🚀 **merit & beyond**

Copy your readme to https://luciopaiva.com/markdown-toc/ to make a table of contents.  This will help assessors to see the structure of your readme. Just test it out ast this tool isn't perfect. It tends to mess up with special characters like dashes.


- [Tic Tac Toe](#TicTacToe)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Author](#author)
  - [Table of Contents](#table-of-contents)
  - [How To Play/Use](#how-to-playuse)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Flow Chart](#flow-chart)
  - [Data Model/ Classes](#data-model-classes)
    - [Class X](#class-x)
  - [Libraries used](#libraries-used)
  - [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [Manual Testing](#manual-testing)
    - [Defect Tracking](#defect-tracking)
    - [Defects of Note](#defects-of-note)
    - [Outstanding Defects](#outstanding-defects)
    - [Commenting Code](#commenting-code)
  - [Deployment](#deployment)
    - [Requirements](#requirements)
    - [Gitpod](#gitpod)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)
    


====================================== The Sections you Fill in are below ==============================

# TicTacToe
![logo](https://user-images.githubusercontent.com/79640465/213293983-f2800deb-8666-4b7b-83f2-0208be2e245c.png)


https://user-images.githubusercontent.com/79640465/213295225-8ea841c3-7e41-4d6f-a88d-741eeb8306a7.mov




## Live Site


[TicTacToe](https://tic-tac-toe1.herokuapp.com/)

## Repository


- [ocimar84/Tic-Tac-Toe-](https://github.com/ocimar84/Tic-Tac-Toe-)

## Author


Ocimar_Felipe

## Table of Contents
🚀 **merit & beyond**

Generate after readme is complete by copying and pasting your readme from this point & below into this tool:
- [mardown table of contents generator](https://ecotrust-canada.github.io/markdown-toc/)
**NOTE:** It does have some bugs if you have dashes or trailing spaces in your headers

## How To Play/Use


- This app was developed as part of my third Portfolio project with the Code Institute. It is a Tic Tac Toe game developed with Python as its only language and is a Player vs Computer style game that are chosen by the user. The user can then play against a computer that chooses its moves at random, or a computer that maximizes its wins while minimizing its losses. In the end I incorporated the google cloud spreadsheet to show the result of all matches.

- The explanatory video of how the system works:



https://user-images.githubusercontent.com/79640465/213564110-03f03512-5d17-4412-8e79-e752ac001e09.mov




## Features


Use this section to itemize the features of your project. 

[Below is a brief presentation of how the game works and the integration with Google Spreadsheet Cloud.](https://user-images.githubusercontent.com/79640465/213560562-1e46ee48-1b08-4509-a542-384bfe9ac287.mov)



### Implemented Features


1 - Logo of the game.

![Logo Tic Tac Toe](https://user-images.githubusercontent.com/79640465/213565871-863ca4ff-90c8-4698-8676-b3e4b1c5347e.png)

2 - Put the name of the player.

![Player Name](https://user-images.githubusercontent.com/79640465/213566286-9b8ce3b3-696e-455b-b478-6ee5eeab2d3c.png)

3 - Machine asks if you want to play?

        1 - Yes / 2 - No

![Do you want to play a game?](https://user-images.githubusercontent.com/79640465/213566672-9441038a-3472-484d-8ebf-70d1635796fa.png)

4 - Player selects houses using the numerical keyboard from 1 to 9.

![Tictactoe](https://user-images.githubusercontent.com/79640465/213566994-d8eb30f1-3c0c-45be-aab9-b66517248923.png)

5 - End the game notifies who was the winner, and it shows that the result is being sent to google cloud spreadsheet.

![winner](https://user-images.githubusercontent.com/79640465/213567172-1ed10f82-cd6f-4e66-8902-87abda532f4f.png)

6 - Ask if you want to play one more time.

        1 - Yes / 2 - No

![one more time](https://user-images.githubusercontent.com/79640465/213567481-d33e6301-1075-49f3-80f8-7f10b1503189.png)



### Future Features

- Use more colorama features.
- Vary tic tac toe layout.
- To give the user the option to choose which tag to start with.



## Flow Chart


- Flow Code chart.

<img width="988" alt="Chart code" src="https://user-images.githubusercontent.com/79640465/213575130-23859527-a858-4b29-9d4b-4916400d327b.png">

- Flow Game Chart.

<img width="963" alt="Game flow chart" src="https://user-images.githubusercontent.com/79640465/213576002-bea09677-ea13-4a7b-b7de-894af70e6888.png">


## Data Model/ Classes


### Board

- **get_board** Metod get board the game

### BasePlayer
- Base player is a generic representation of a player.

#### Properties
- Marks the symbol to be used to represent player X or 0.

#### Methods
- **available_moves_display** Method to choose a move based on a game board.

### ComputerPlayer
- Computer player is the computer in the games.

### Player
- The human player determines his movements using the base player.

### TicTacToe
- Basically the game TicTacToe

#### Properties
- **board** an array of 9 entries representing positions.
- **current_winner** tracks whether a player has won the game or not.
- **computer** player representing the computer.
- **player** player that represents the human user.

#### Methods
- **game.printboard()** Prints out the game board to the terminal.
- **game.playerinput()** Enter the player's name and ask if he wants to play. (1 - yes / 2 - No).
- **game.checkifwin()** Places the player tags according to the index provided. If the index is an empty square, return True and make the move. If the index is occupied, return False and invalidate the move.
- **game.switchplayer()** Change who is playing by switching between the player and the computer.
- **game.computer()** Computer randomly selects your position on the board.
- **game.checkifwin()** Places the computer's tags according to the index provided. If the index is an empty square, return True and make the move. If the index is occupied, return False and invalidate the move.

### Class X
- **class TicTacToeGame()** Used to determine the python class.

**Python Libraries**
- Random: used to randomize the computer's moves.
- Colorama: used to color the game throughout.


## Testing

![Code TicTacToe Game ](https://user-images.githubusercontent.com/79640465/213772339-fcf76435-aa51-470a-9c87-ab779ae7a6cc.png)

![Code TicTacToe](https://user-images.githubusercontent.com/79640465/213772365-5361c014-4701-478b-a291-175716ac6e78.png)

![Code run](https://user-images.githubusercontent.com/79640465/213772396-52bfb2bf-b23b-4901-9194-ad207c3ee4cf.png)

### Validation Testing
🚨**Required** 

You should try to ensure you code is valid and follows proper indentation.  In this section you should write up any websites you used to validate your code. As your projects becomes more complex these tools may change.

For each python file in your project, paste it into [CI's pep8 tool](https://pep8ci.herokuapp.com/), and take a screenshot of the linter output showing NO ERRORS

![image](https://user-images.githubusercontent.com/23039742/212106175-36b2f18a-7c75-458d-94dd-9886e81c71f3.png)

Ideally you would have no errors remaining outside of line too long which you can fix by 

adding
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

Note any errors or warnings you are ignoring and why.

### Manual Testing


### Manual Testing

- You will find my manual testing sheet [here](https://docs.google.com/spreadsheets/d/123dAl30RBw5Sq-1GjS7DWu6I563MDM4ZSPRLnatv-ss/edit#gid=0)

### Defect Tracking

- You will find my defect tracking sheet [here](https://docs.google.com/spreadsheets/d/1xYKKoZuA54QKtIxZ2fA6-BUdHOFavs1R6JX9CK3YZQM/edit?usp=sharing).

### Defect Tracking

![Defects](https://user-images.githubusercontent.com/79640465/213796712-c17f19b7-83b2-457e-9349-a3b7cbd3bab7.png)




### Outstanding Defects
🚨**Required** 

It's ok to not resolve all the defects you found as long as:
- it does not impact a user from completing a vital function on the website
- it only affects a very small subset of users
- is an extreme edge case that very few users would try
- there is an open issue against a framework, browser or technology used

If you know of something that isn't quite right, create an issue and link to it here and explain why you chose not to resolve it. 

Sometimes it's as simple, word wrapping issue that makes the site look odd at a certain screensize that you just didn't have time to fix due to the impending deadline it's best to mention it but note why you allowed it to go live: "Yes it looks odd, but it doesn't impact core functionality of the site." than to let the accessors think you didn't notice it. 

### Commenting Code
🚀 **merit & beyond**

Make sure you use triple double quotes to document functions and classes.
 Here'a  documentation worthy example:
```$python
def yes_no(question):
    """
    Function to ask a simple yes no question of the user.
    :param question: String displayed as the question
    :return: answer: String equal to "1" or "2" representing yes or no respectfully
    """
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1", "2"):
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer

```

## Deployment
🚨**Required** 

### Requirements
🚨**Required** 

If the user is required to have certain keys and credentials you should include this section with directions on how to get the necessary information.
ex)
1. **Google Account:** In order to have this program work, you need a google account. If you don't have one  [Create a google account](https://accounts.google.com/Signup)
2. **Google APIs**
    1. in a new incognito tab, log into your new google account.
    1. then update the url to be: https://console.cloud.google.com/getting-started?pli=1 
        
        **GOOGLE DRIVE API Access**
        1.  create a new project for this, call it XXXXXX (You might want to refer to what you see in this video: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/ at the bottom of the screen to write out steps.)
        2. Then click on Add APIs and Services and select Libraries
        3. Search for Google Drive
        4. Click Enable
        5. Click Create Credentials
        6. Select Google Drive API from the drop down, Application Data, then no and click the Next Button
        7.  (https://developers.google.com/drive/api/v3/enable-drive-api) 
        8. for service account details fill in a service account name ex) xxx_API, then click Create and Continue
        9. For the Accoun acces, select Role: Basic/Editor then continue
        10. Then Click Done
        11. Now select the newly created service account
        12. Click on the KEYS Tab
        13. Click Add Key
        14. Select JSON type (right click to show in folder so you know where the file was saved.
        
        **GOOGLE SHEETS API Access**
        You may need to us the back button get to the APIS & SErvices section from where you were.
        1. click the Libray  Tab and serarch for Google Sheets
        2. click enable

3. The downloaded credentialsJSON file is basically your creds.json file that you need to put into your heroku settings or gitpod environment to access your google drive.

4. Google Sheet Template
  - If you had to create specific sheets for your project, instruct users to make their own copy of it from yours and rename it back to what the python project expects
  - And don't forget to share the spreadsheet in question with the client_email from the creds.json 

### Gitpod
🚀 **merit & beyond**

This section should describe the process someone would have to go through to get the local working in gitpod.  Such as install requirements.txt  and setting up a creds.json file that is in the gitignore and keeping their workspace.

If you have project settings required such as a creds.json file from the GOOGLE DRIVE API acess, please provide an example of that file in the writeup with the project key values:
```$python
{
  "type": "service_account",
  "project_id": "ocimartictactoe",
  "private_key_id": "b6869f37eb1a62a2896caee1903d1c4286b84dea",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC1OJYZeSXJ8Pdk\nfnYW5W+1+uBurbXQMf6Rw8zJ8y7W86MKBAO4BmChCX1xOi9ZbyQO4zGu1LjkRfDj\n3ggxuoknyEPU5vutgaUiK3Yi2NJSLEc/q2nRsvaDyOLxkrmOV802XUGfZpx03JpD\n9Hqu3z0IZggEi+ujv97ncTa5/Ik30+TZL288tlwuzWuf4n2HhZtNCNGLaa2hTJL0\ndoyidKqyAV/YiyxaW+nRj7ynW44XSK7H1QncnpegL4stWlTVUkLhZLSsnS38jBFN\n14J5+4P/WZVEAG06KT3bS1cFs/QFeXe/7bCS28t+/musrrMnmOiLyPnBVV//yQqd\nW0+3qScZAgMBAAECggEAEYbN1YbcUGySsKXJFqvNTboGwg2LhlLffl+DyzWkHmaP\n1SR665hfo2jUjgKE7nm2Rg5TvByXXn8j2MCc5ZpXMNbIi1W6ROyYo6EKcD0CElp1\nRZjMHNuEcKMZd9MAnoiqsIr9EW/jdStEwYpqjHEgvlLdNvtaqIqiV0X2zK66OADc\nxMsLOufvPAR5HUt/Jrc+GqDahBQ7x6ycbfivU8bVcS0CjjMry5YY2e0UUVXlVAgS\nooNnkoKm/5+ZReZ3SptJ9XUXjNHCa8Aw5zMvYc/R1zD9ZiazlkH4YinUR0txaIqW\n2ijOKWop/WogLT8SKjPrOD2kPBxcwbVfmBia+rq/lQKBgQDt0q0BY0mk7oGggZFY\nFNxO+SDS7pJx1BDlEQtmrBMV+85MmlKZaQ1EEfOaj0Em0oIvSdJK+NY3Hvt2kWPK\nA2nCFxcaQKhop+an+b1hSTWCY7aox5C4Usmst69K01vp7eXh71wkFJjvMiIFc310\nZ/0EO4t1pjw5lVFYIliKpC4zowKBgQDDEmscMqokXwRhS3KHtMakNNJd+WVa9Xw+\nbl26HkCS+X8cpS8cEtkY6RelmRWENCVRfgJWm78NrqvFcJUI+rRrKlVDbVEeIDWy\nDbokOEcXM8aanI4d52Cy6ZolHJzA3f6/qwU8wZAz8sLxl2WWGWQEPcm90Yn2XQaz\n+Cs1tTyGEwKBgQCjFznbXMpxF7q/ZntU6yFV6xSucjrtYp+fZvvpkhGYntEPyTjh\nyZ/2UVU8Zgco522tnjNfhJvquw15dyT2sTaCirEmKLcU5ieQg/xyTfErFNR7lDfT\nn7p7/o9wgddjaeie8zW97H4gcsHP+S5MeM+Tan4t1S0x1AsvpIYRtZuVfwKBgQCU\nTUxhA6OWQyZxUYqg4S6jaAUGrLQBkuACFqXq+VTeaA/bFznZffrOlWcE3n0dJQe6\nDLJ6Za26GTE9yXmEehTv5B8uQ82HubUYyJbbMm3ZleNHZ/4jfeRmIHKwBDCn8B3c\nWYiByCZ5V/Yc9ZyloGgJUXAufz8DrXWLHQC8tCxvQQKBgQDA+5fXk4DHWNl5b1DI\nApTGN1+JBbf3q/UtYn9pyJvSbSYbChIvSToAIz/2rJ8L27A1TPhVCY2Mrwjdlwzu\n8ia1pN4Sq1oCPxVBcwl//s5YyHzZtZbAIoQwZBff1SAZmqw9bitncJ9maazw3PoZ\nswguIH/g+OpM3DDUz+MVQbFPxA==\n-----END PRIVATE KEY-----\n",
  "client_email": "ocimartictactoe@ocimartictactoe.iam.gserviceaccount.com",
  "client_id": "109103238029005579935",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ocimartictactoe%40ocimartictactoe.iam.gserviceaccount.com"
}
```

If you have any dependencies, you should instruct users to install them
```$python
pip3 install -r requirements.txt
```

### Heroku

- Head to [Heroku](https://heroku.com) and create an account.
- Click on "Create New App".
- Name your app, select your region and click on "Create app".

![App Information](https://user-images.githubusercontent.com/79640465/213801784-d297000c-6d93-4f8a-bc7b-15663bec15cd.png)

![ocimar84:Tic-Tac-Toe-](https://user-images.githubusercontent.com/79640465/213802257-4401e55e-2f58-4da3-99a5-18e8031ffbe2.png)

![Config Vars](https://user-images.githubusercontent.com/79640465/213802674-4a9c47d4-4d03-4512-a685-d463877c6d6f.png)

![B  Build Packs](https://user-images.githubusercontent.com/79640465/213802748-13b8e36b-82d9-4e9d-81e4-104420d62991.png)

![Deploy A](https://user-images.githubusercontent.com/79640465/213803017-700897f4-ac90-4c85-a7f4-9b4aabeef4c2.png)

![B  Build Packs](https://user-images.githubusercontent.com/79640465/213803042-ec7a32d6-28ba-4484-9593-2729434c3800.png)

![Deploy either manual or automatic](https://user-images.githubusercontent.com/79640465/213803054-eab55616-ab4c-4dfc-9707-9eb41fe436b3.png)



## Credits


-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content
🚨**Required** 

[Use bullet points to list out sites you copied text from and cross-reference where those show up on your site](https://www.geeksforgeeks.org/print-colors-python-terminal/)

[https://realpython.com/documenting-python-code/]
(https://realpython.com/documenting-python-code/)

https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/

https://www.scraggo.com/python-classes-guess-the-number/

https://www.geeksforgeeks.org/print-colors-python-terminal/

### Media
🚨**Required** 

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments

I would like to thank all the knowledge that was acquired and make a comment, I had a lot of difficulty in finishing this project, I found the classes confusing, I had to look for another type of help to understand. I had a serious problem on my machine where once again github was not pushing.

I would like to thank my mentor Malia who was very patient in explaining things to me more clearly.

Andre Maurilho helped me configure my computer so that github would work, and even uploaded a file that was stuck in my repository.

