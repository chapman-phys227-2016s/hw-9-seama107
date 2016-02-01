# Instructions

## This Assignment

* Clone this repository to your local machine.
* Edit the README.md file according to the instructions below.
* Perform a ```commit``` so our local repository remembers the edits you've made
* Now push the results back to the github repository

## General

* Edit the README.md file:
    * Change _\<your name\>_ and _\<date\>_ at the beginning of the file
    * Edit the line ```[![Build Status](https://travis-ci.org/chapman-phys227-2016s/UPDATETHIS.svg?branch=master)](https://travis-ci.org/chapman-phys227-2016s/UPDATETHIS)``` replacing both instances of ```UPDATETHIS``` with the name of this repository (should be something like ```hw-1-<your git name>```)
    * Reread the __Honor Pledge__ again and 'sign' it with your name at the end
    * Add your own text in the __Assessment__ section

* Connnect the repository to Travis CI
    * On the github site, go to ```settings``` then to ```Webhooks & services```
    * Then click on ```Add service``` and scroll to ```Travis CI```.
    * This takes you to a new page. Scroll to the bottom and click ```Add service```

* Correctly document each source file
    * At the top of each source file (```.py``` file), include a docstring in the following format

    ```
    """
    File: <filename>

    Copyright (c) 2016 <your name>

    License: MIT

    <brief description of the code>
    """    
    ```

* Ensure that what you push to the github repository builds correctly (the build badge displays as [![Build Status](https://camo.githubusercontent.com/c71f5665277589f9ba8039c6e1b8bb120a3640b2/68747470733a2f2f696d672e736869656c64732e696f2f7472617669732f436861706d616e43505343323330537072696e6731362f41737369676e6d656e742d582e737667)]()) in the README file.
