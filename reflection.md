# Reflection
## Problems and Struggles
    - Input and State became harder to cleanly build now that 'Ui Navigation' got involved.
        - Planning to solve this with 'Ui Screens' or 'States' akin to a StateMachine.
    - Struggled with error handling for screens.
        - Solved this by creating an 'error' screen that reads the most recent error.
    - Struggled with the initial structure of Screens and the ScreenManager.
## What I learned
    - This is the first time I used a 'StateMachine' or something with the likeness of one.
    - This is also the first time I learned to query REST Api!
## What needs to be improved
    - The 'Screen' system is prototypical and I am unsure of its viability.
    - The 'State' object can become a god object if it stores 'every' state.
        - Should be limited to things that are only needed across screens?
            - Perhaps data should be sent to the screen during transition
              instead of everything living in the same 'State' object.