Amazon Clone
**Home Page**
 

    1. Showing all products (title and price)

    

**User Registration Page** 
 

    1. User Registration
    2. User Login
    3. User Logout

    

    

**Product Landing Page**

    1. Showing product title, description, regular price, discounted price of a product
    2. Click on add to cart button to add item  

        

**Cart Page** 

    1.Clicks on cart
    2.Cart details along with subtotal for each product(quantity* productprice). Also displays grand total for all products with tax            calculation.
    3.User clicks on remove button to remove products from cart.
    4.User clicks on proceed to checkout.

**Checkout Page**

     1.User enters details on the form and clicks make payment.
     2.Email and text notifications are sent to user on payment.

**Orders Page**

     1.User sees current order details.

**Admin Page**

    

    1. Admin users can see a list of options available to them:
        - Products
        - Users
    2. Products
        - CRUDE
    3. Users
        - Read (view-only)

**CI/CD: Flask App + GitHub, CircleCi, & Heroku**

	1.Create a GitHub repository for our project.
	2.Code our Flask application with the Python Flask Framework.
	3.Push our Flask application to GitHub.
	4.Add automated tests to our Flask application
	5.unittest and pytest for testing code logic
	6.Flake8 for testing code style
		(We won’t do integration tests in this tutorial.)
	7.Set up Travis CI to run our automated tests for each commit
	8.Create a Docker image to package our Flask application
	9.Push Docker image to DockerHub.
	10.Deploy Docker image to Heroku.
	11.Set up Travis CI to automatically run all tests, create a Docker image, push the image to DockerHub, and Deploy Docker to live servers on Heroku. This process will be done automatically for each commit to our GitHub repository.

#### pipenv environment variables

``` console
set PIPENV_VENV_IN_PROJECT 1
```

#### To run application

``` console
set FLASK_DEBUG 1
set FLASK_APP <aoutapp.py absolute path>

```
