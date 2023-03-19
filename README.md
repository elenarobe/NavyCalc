# NavyCalc
Generally speaking, the code implementation is the written text using a the format and
syntax of a programming language. In our case, the chosen programming language was
Python. Python is a dynamic, multi-paradigm, object-oriented programming language,
that emphasizes code cleanliness and simplicity. Its syntax allows developers to express
some programming ideas in a clearer and more concise manner than in other
programming languages, such as C++.
For the development of NavyCalc, there was used PyCharm Community, which is a
free development environment for Python users, offering a wide range of essential tools
that serve to achieve any proposed goal.

NavyCalc software is comprised of 4 windows, “Home”, “Example”, “Help”, and
“About”, each with a different structure and functionalities, adapted to the requirements,
which together aim to provide a good user experience.

## Home window. 
The home window, suggestively named, is the window that will
appear everytime the application is opened. It is comprised of a variety of buttons, tables,
labels, and a 2D chart. In the upper left corner, the menu can be found, which consists of
4 buttons: “Home”, “Example”, “Help”, and “About”., with which you can navigate
between windows. Also, the title is located on the top of the page, which was chosen in
such a way as to concisely explain the functionality of NavyCalc. The two buttons, “+”
and “-“, help the user choose the number of sequences that the problem has. Following,
the user has to enter the data that is provided in the first table. It should be noted that a
certain data entry is required. For the sections corresponding to latitude and longitude, we
will have the following form: “degrees-minutes-seconds.decimals”, immediately followed
by the initial corresponding cardinal point (N for North, S for South, E for East, V for
West), i.e. “43◦12’12.13N” will be written as “43-12-12.13N” in the corresponding cell.
In the column for time, the value will be written in the format “hh:mm:ss”, i.e.
“12:30:00”. The rest of the columns, do not require any special format. The boxes with no
provided values, should be filled with “0”.
Once this is done, by clicking the button “Calculate”, all the corresponding answers
will be displayed in the second table, along with the value of the magnetic declination and
a simulation of the map drawing in the two-dimensional graph.
![image](https://user-images.githubusercontent.com/121317737/226164133-1ec1b587-be2e-4afa-8592-a78fc617b97c.png)

## Example window
This window contains, as the title says, an example of a
solved dead reckoning problem, more precisely, the final shape of the window, after
pressing the “Calculate” button.
Regarding its composition, it has the same elements as the “Home” window.
In order to navigate to this window, one must press the “Example” button, located in
the upper left corner.
![image](https://user-images.githubusercontent.com/121317737/226164648-df064d45-c731-4ee1-868f-4c99978ea803.png)

##Help window
This window contains all the information you need to know in
order to use NavyCalc.
It consists of a series of tags (QLabel), used to write the text.
In order to navigate to this window, one must press the “Help” button, located in the
upper left corner. 
![image](https://user-images.githubusercontent.com/121317737/226164689-c79a97c2-d43c-46c7-87c5-1db7006c485a.png)

##About window
This window contains information regarding the purpose,
development and the author of NavyCalc.
Its components are similar to the previous window presented.
In order to navigate to this window, one must press the “About” button, located in
the upper left corner
![image](https://user-images.githubusercontent.com/121317737/226164719-1e9fb44d-266e-466d-b328-433e8f5a24e2.png)

## Conclusions
In conclusion, the purpose of this project to develop a modern way to solve dead
reckoning problems through a completely functional and responsive software in order to
make the students' and professors’, any any other users lives easier.
