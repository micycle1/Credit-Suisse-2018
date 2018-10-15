
# Credit Suisse Coding Challenge 2018

Welcome to the Credit Suisse Coding Challenge 2018. Below are instructions for getting started on the Challenge!

### Competition Rules


Challenge Questions are available on our website at www.credit-suisse.com/codingchallenge.

To get started, first fork this repository in order to obtain your own copy. Please note that per Challenge rules <b>this repository must be visible to us (CS-CodingChallenge)</b>.

This can be achieved by either keeping the repository public, or by adding <insert username here> as a viewer to the private repository.

### In your repository

You'll find several files in your repository, most of which you shouldn't touch - these are set out below:

- <b> Do not modify or delete files <i>Procfile</i> and <i>vcc-skeleton.py</i>.</b>

- You may add new Python packages. To do this, add new dependencies to your <i>Pipfile</i>, ensuring not to delete any lines that are already present.

- Please note this skeleton is written using Python 2.7. This is the only Python version available in the Challenge.

- A guide to adding Pip dependencies can be found on the Pip website.

- To add code to be run, modify the files q1.py, q2.py, q3.py, q4.py q5.py and q6.py.

### Deploying your solution

In order to submit your code to the Automated Evaluator, it first needs to be deployed to Heroku. For this, you'll need to create a Heroku server:

#### Connecting Heroku to your Git repository

1) Set up a Heroku account. This is free, and can be set up at www.heroku.com
2) Download the Herou Command Line tools (www.devcenter.heroku.com/articles/heroku-cli)
3) In a command prompt, log in to your Heroku account using the command:
    <code>heroku login</code>
4) Navigate to your git repository in the command prompt.
5) Run:
    <code>heroku create</code>

#### Deploying to Heroku

1) If you have added any dependencies to your solution, ensure they are in your Pipfile. Failure to do so will result in your Heroku server failing to run.
2) Add files to be deployed to Heroku using <code>git add "file-name"</code> 
3) Commit the files for deployment using <code>git commit -m "Your commit message here"</code>
4) Deploy to Heroku using <code>git push heroku master</code> (Please note, this doesn't push to your original repository, so remember to push your changes there as well frequently).
5) Your solution will be deployed to Heroku. You can see the logs to your server using <code>heroku logs --tail</code>

<b>Please note - for your solution to be considered valid, you must grant access to your Heroku server to challenge.coding@credit-suisse.com</b>. This can be done on the Heroku website.

#### Tell us you've deployed

At our website, we have a tab listed <i>Register Heroku</i>. Here, you should tell us your Heroku name, and GitHub repository address. To start the process, you'll need your UserID (provided in your starter email) and the email address you signed up with. Once this is complete, please allow an hour for your score to be updated on the leaderboard. You only need to complete this step once.
