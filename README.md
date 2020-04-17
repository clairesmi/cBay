![CS Icon](/readme-assets/favicon.ico) 

# cBay

I have recently started to learn how to use Vue, transferring my skills from React and learning about some of the differences between the two frameworks. I also wanted to practice using Django, specifically working with multiple models with related fields, so I set myself the task of creating a mock up of an online second hand clothes shop. I also decided to have a go with CSS Tailwind.

[insert homepage image here]

## Deployment
The project is deployed with Heroku and cn be found here: https://cbay-online.herokuapp.com/


## Getting Started

If you would like to login to the site to have a look around you may use these details:

email: carla@email.com

password: pass

### To download the project:

Use the clone button to download the source code. Enter the following commands in the CLI:

To install all the packages listed in the package.json:
```
$ yarn
```
To activate virtual environment: 
```
$ pip install pipenv
$ pipenv shell
```
To install all the packages listed in the pipfile:
```
$ pipenv install
```
Run the app on localhost:8080: 
In virtual env:
```
$ yarn back
```
In a separate terminal tab:
```
$ yarn front
```
<!— Check the console for any issues and if there are check the package.json for any dependancies missing —>

<!- Navigate to http://localhost:8080/>

Compiles and minifies for production:
```
$ cd frontend yarn build
```

## Technologies Used:

- Vue CLI
- Vue Multiselect
- JavaScript
- Django
- Python 
- HTML5
- CSS3
- Tailwind CSS
- CSS Animate
- Axios
- Yarn
- Cloudinary (for image upload)
- Jest

## User Experience

[insert user journey image here]

### Buyer

The user lands on the homepage where they are encouraged to sign up or login. 
They are then able to browse the site from a choice of two index pages. If they click on 'Go to Listings' in the nav bar then they will be able to view and filter all listings. If they click on one of the carousel images then they will be able to view all items in a specific category. 

From here, the user as a buyer can then view the individual item page and they have the choice to put it in their basket.

In the nav bar, there is always the option for the user to go to their basket or their profile, from the basket they can then go to the checkout to 'pay' for the item or they can remove the item from their basket and it will become available again on the listings index page. 

The user also has the opportunity to edit their profile, specifically they can upload a profile image or they can update heir email address but they are not permitted to update their user name.  

[insert screen shots of basket page and profile edit page]

### Seller

From a selling perspective, the user always has the option to list a new item available to them in the nav bar once they are logged in. 

They can post and edit items through the listing form.

[insert listing form image here]

## Challenges 

Snippets:

[code for Django partial update]

[event bus code]

[code for basket field on item model with user ID]

## Reflections and Future Improvements

Notes to be filled out:
- add reviews
- add filter by price
- add auto complete component on search bar