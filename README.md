# Password Repository v0.0.0


## First Steps
That's the first view of my Password Manager program.

Here I'm going to include all versions I'll make and something I'll have learned on this journey.

Today I've learned about 'decode' and 'encode' methods.
By the time, I've had success when I tried to encrypt some information and I can say I'm happy about it.
I hope keep learning about this project!

With OS module, I've learned to create new directories and move different type of files.
Function 'open()' had helped me to create new files I'll need on future.
At least I could end my new function 'install'.

Finally, with a lot of doubts resolved, I manage to do the base program. After this point I can achieve work in updates and minor changes.

## New (and interesting) 'Problems'
This time I was testing this program when I realized it's something wrong:
If a new user registers on platform there isn't a problem, but when the new user tries to add a new password with the same name as the main user, it overwrites the main file!
This problem it could be solved by add a database file linked to each user registered so, this time I'll try to work with SQLite language and libraries.

I think the best way is to have two libraries. One of them for user data where I'll keep all new users and its passwords (this library advice to you if the name's user is registered too).
The other one will be linked to each user and it will keep all user passwords.
