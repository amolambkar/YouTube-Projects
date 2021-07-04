# Create Jokes Using Python
#### pyjokes library

Hello Techies,

Now-a-days most of us love  to read jokes for programmers. In this tutorial I will explain you how one can create a joke for a programmer using python.

Video Tutorial is available on my YouTube Channel **Tech Blooded**
 [Tutorial](https://youtu.be/TkNcc_CAzpw) 


[![Pyjokes Tutorial.png](https://raw.githubusercontent.com/amolambkar/YouTube-Projects/main/Pyjokes/Pyjokes%20Tutorial.png)](https://youtu.be/TkNcc_CAzpw)


Python supports creation of random jokes using one of its libraries. That library is **pyjokes**.

Pyjokes is a python library that is used to create one-line jokes for programmers. Informally, it can also be referred to as a fun python library which is pretty simple to use. Let us see how we can actually use it to perform the required task. And the task is to create jokes.

We can simply install it using the following command

```
pip install pyjokes
``` 


Use following code to import it in your python script . 
```
import pyjokes
``` 
And by importing that library to our python script we can use it in our code.
So to create a joke we can use get_joke() function , this function has 2 parameters :

- language of joke
- category of joke


Possible values for language parameters are **English , German , Spanish , Italian , Galician** and **Basque**. And the default value is **English**.

Possible values for the joke category are **Neutral , Tongue Twister** and **All**. And the default value is **Neutral**.


1. Using the ***get_joke()*** function we can generate a single joke.

```
#create a single joke
#language is english and from neutral category
joke = pyjokes.get_joke(language='en',category='neutral')
``` 

2 . To generate the list of jokes we can use the ***get_jokes()*** function.
In this function the parameters are the same as the previous function.

```
#create list of jokes
joke = pyjokes.get_jokes(language='en',category='all')

for i in range(5):
    print(joke[i])
``` 

So now you can generate a joke anytime you want with your python skills.

So Techies,
I hope you all understood the tutorial to generate a joke and list of jokes using pyjokes.

If you loved this article , please show some love by subscribing  [My page](https://hashnode.com/@amolambkar)  and  [YouTube channel](https://www.youtube.com/channel/UClhbnKEAywXqkLkxa_23j0Q) .

For more articles visit my page [Amol Ambkar](https://amolambkar.hashnode.dev/)

