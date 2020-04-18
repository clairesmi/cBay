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

One of the main challenges I faced working on the backend was enabling the user to edit their profile. Due to the fact that my user serializer was implementing a password check on sign up and login, I needed to use a different context to allow the user to be able to edit their profile without entering and confirming their password again. 

So after doing some research and reading some of the Django documentation, I wrote the edit profile view as below, setting the context.

```
def put(self, request):
        user = request.user

        # set the context to edit so password & confirmation are not needed & set partial

        # to true so that the user can edit their chose fields without editing every field on the object

        updated_user = UserSerializer(user, data=request.data, context={'is_edit': True}, partial=True)
        if updated_user.is_valid():
            updated_user.save()
            return Response(updated_user.data)
        return Response(updated_user.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)
```

I then wrote an if statement in the User serializer specifying what to do if the context is edit - return the data without doing the password check.

```
   def validate(self, data):
        # if context is edit, do not require password & confirmation

        if self.context['is_edit']:
            return data
```


Another challenge I came across was understanding how to make the nav bar reactive, so that when the user logs in or adds something to their basket, the nav bar updates to show the new options available to the user after logging in, or the number of items in their basket.

So after doing some research into how to achieve this in Vue, I decided to use the Event Bus functionality. 

I exported a new Vue instance called eventBus which I created in my main.js file which is the route of the app that is mounted into the index.html file. 

```
export const eventBus = new Vue({
  methods: {
    loginCheck() {
      this.$emit("userLoggedIn");
    },
    updateBasket() {
      this.$emit("basketUpdated");
    },
    removeFromBasket() {
      this.$emit("removedFromBasket");
    },
    calculateBasket(data) {
      this.$emit("calculatedBasket", data);
    },
    emptyBasket() {
      this.$emit("basketIsEmpty");
    }
  }
});
```
I put my methods inside this Vue instance so that they can be used to emit certain events which can be listened to by any of my other components. 

The most complex method I created was the calculateBasket method. 

This created function in the Basket.vue component listens for the userLoggedIn event which is emitted by the login component. When the basket hears this event, the event bus function calculateBasket is called with the length of the basket items array passed in as a parameter. This means that the correct amount of items is shown in the user's basket when they login (which is useful if they have logged out with items still in their basket).
```
created() {
  eventBus.$on("userLoggedIn", () => {
    eventBus.calculateBasket(this.items.length);
  });
```
The Navbar.vue component then listens for the calculatedBasket event and has access to the parameter passed in through the calculateBasket function. 
```
eventBus.$on("calculatedBasket", data => {
  this.itemsInBasket = data;
});
```
Within the Navbar.vue component the data property itemsInBasket is set to point to the same value that is emitted from the calculateBasket function. This data property is then dynamically updated within the template and displayed as the shopping cart with a number on it. 
```
<p class="text-white">{{ itemsInBasket }}</p>
```
The final challenge that I want to highlight is in deciding how to use the database models to show that an item is in a user's basket. I considered created an array of item ID's on a basket field within the user model but eventually settled on creating a basket field on each item which would contain the user ID.
```
class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    size = models.CharField(max_length=50, default='')
    image = models.CharField(max_length=500)
    buyer = models.CharField(max_length=500, default='')
    categories = models.ManyToManyField(
        Category,
        related_name='items',
        blank=True
    )
    owner = models.ForeignKey(
        User,
        related_name='items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    basket = models.ForeignKey(
        User,
        related_name='basket_items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    purchased = models.ForeignKey(
        User,
        related_name='purchased_items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Item {self.name}'
```
I found that this may have been a cleaner way of adding and removing each specific item from a user's basket, as I was able to filter through the items and look for a basket ID matching the ID of the currently logged in user in either the frontend or the backend. 
```
class BasketListView(APIView):
    def get(self, request):
        user = request.user
        basket = Item.objects.all().filter(basket=user.id)
        serializer = ItemSerializer(basket, many=True)
        return Response(serializer.data)
```
```
async getBasket() {
  try {
    const res = await axios.get("/api/basket");
    this.items = res.data.filter(
      item => item.basket === Auth.getPayload().sub
        );
  } catch (err) {
    this.$router.push("/notfound");
  }
},
```


## Reflections and Future Improvements

This project was a challenge for me and I'm happy that I have pushed my understanding of Vue. I really like this framework and I will aim to become more efficient with using it in the future. I think that Vuex will be the next aspect I aim to learn. 

Specifically for this project, areas where I think I could add some more interesting functionality are:

- adding user reviews so buyers and sellers can comment on their experiences.  
- add a draggable filter by price bar
- add an auto complete component on search bar