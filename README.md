# __Henna Styles__

The past year of worldwide lockdowns has inspired many people to take up new hobbies and attempt beauty treatments at home,
 as they could no longer visit professionals. Henna Styles is an online henna shop and art community, which provides a range 
 of henna products visitors can purchase as well as providing a platform for people interested in henna design to improve their
 abilities and learn from each other.

- - - 

## __UX__

### __Value provided:__
#### __For users:__
- As a visitor with no previous experience with henna I would like to know more about it before purchasing.
    - The homepage will address this as soon as a visitor lands on the site. The homepage will contain a link to the community 
    section and shop so visitors can find further information or go straight to the shop. 
- As a new user I want guidance on how to use the products effectively
    - The community section will address this. People will be able to view henna related posts from other users and the site 
    owner. Knowing more will encourage them to make purchases and experiment with extra products. In order to ask questions of 
    the community however they will have to create an account.
- As a professional user and want to find a range of products in one place
    - The homepage will contain a link to the shop and the types of different products will be displayed on the navigation bar 
    throughout the site so visitors can find what they are looking for quickly from anywhere.
- As a user who has some previous interest in henna I want to know what I have purchased before so I can repurchase easily
    - When making a purchase customers can create an account which will hold their preferred shipping details and an order history. This will be available only by logging in when making a purchase.
- As a professional user I want to see others work for inspiration
    - Community page will allow people to view others' work, however to gain the full effect of the community (respond to 
    and create posts), users will have to log in.
#### __For store owner:__ I want to maximise sales.
- I want to make sure all visitors know the range of products being sold.
    - Site navigation will contain the main types of products sold and will be available throughout the site.
- I want the user to have a positive response to the site and spend longer on it as this will motivate return visits.
    - Users will be able to view the community page which will produce a positive response and lead them to stay on the site longer. They will be made aware that they must create an account to access all actions on the page.
- I want to increase the number of visitors who return to the site in order to gain repeat purchases.
    - The community page and order history increase the likelihood customers will return, either to view new posts, 
    comments on posts that interested them or simply repurchase a product they liked.

### __Wireframes__
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the 
design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory),
 or just hosted elsewhere online and can be in any format that is viewable inside the browser.
 
+ [Home wireframe](documentation/wireframes/home-wrf-img.PNG)
+ [Shop wireframe](documentation/wireframes/shop-wrf-img.PNG)
+ [Community wireframe](documentation/wireframes/community-wrf-img.PNG)
+ CHECKOUT view
+ PROFILE view
+ Add/Edit post view

### __Overall design__
+ In order to get an idea of the conventions of shopping/blog art sites I visited several online stores. The styling is simple
 when displaying products but other pages are loaded with colour and images, creating a positive response. Several of the more popular art 
 supply shops had sections which contained information and blog posts (like jackson art). I also viewed some online henna shops 
 which appeared to be for smaller companies as the style was very simplistic and none offered all the different types of products 
 offered on Henna Styles. Some of the sites used for inspiration include: [Jackson art](https://www.jacksonsart.com/),
 [Desenio](https://desenio.co.uk/), [Henna Shop](https://www.hennashop.co.uk/).

+ The colour scheme used for the site was created with coloors. The colours are simple including black, gray and shades of pink,
this was chosen in order to keep the pages simple while still vibrant and allow image pages to create a strong response in 
comparison. [Palette used](https://coolors.co/ffb6c1-d6d7d7-b27f87-210124-00171f).

- - - 
## Database Schema

Sql was used to create this database.

## ADD IMAGE OF DATABASE SCHEMA

---- 
## Features

###Sitewide Features: 

- __Navigation bar:__
    - Top navigation bar is styled with the sites theme colours and contains 5 links. 
        - The first is the site logo which leads to the homepage. 
        - The next is the search bar, which allows users to search for products from anywhere on the site. 
        - The Account link is next, this displays links relevant to the current user. For anonymous users,
        the links avaliable are 'register' and 'login'. For authenticated users the links avalaible are 'my profile' and 'logout'.
        Superusers will also have access to product management from the account section, where they can add products.
        - The Shopping bag link is next, the shopping bag totals are displayed and updated each time the user
        adds an item to their shopping bag.
        - The final link is for the community page
    - __Bottom Navigation bar:__
        - contains links to different product searches. The user can select a product category or choose to 
        display all products by a preferred sorting method, such as low to high prices. 
        This part of the navigation bar is displayed in full on larger screens but toggles on small screens. 
        On small screens a home link is also displayed.
- __Delivery banner__ reminds user of the free delivery limit, which may incentivise them to buy more.
- Footer
    - Contains links to social media 
- Toasts
    - Toasts are displayed throughout the site based on user interactions. A summary of the bag is displayed when users alter
    its content. Errors and important general information is also displayed through toasts.

### Homepage:
    - __Header image__ is of a desgin being created with henna. The hand being decorated is shown on an ornate box, which complex designs.
     The colours are dark and contrast with the rest of the site, drawing the users attention.
    - __Heading and intro__. The heading is a large welcome message in the logo font and theme pink colour. The intro explains to the user
    what is avalaible on the site.
    - __Buttons__ Two buttons are avaliable on the homepage. One for shop and one for community. This guides users to either make a purchase 
    or view the community page where they can gain some inspiration, which hopefully will lead them to purchase the products.

### Products pages:

    - __All Products__
        - __Sorting dropdown selector__ allows the user to choose from a selection of sorting methods.
        Once a method is selected, a link to 'products home' appears which allows them to reset the search, 
        they are also able to select a new search method from the selector if they like.
        - __Navigation category selection__ when a product category is selected from the navigation bar. All products
        in this category are displayed, links to subcategories are also displayed below the heading, allowing users to 
        narrow their search down further. Again, the product home link is avalaible on these pages to reset the search and 
        the sorting methods to organise the results.
        - __Product Results__ are made up of a large product image, the product name and price and a link to the category
        the product belongs to. Selecting a product takes the user to a product details page.
        - __Edit delete buttons for superuser__ When the user is a superuse, edit and delete links appear under each product allowing 
    them to easily edit and remove products from the site.
    - responsive design
    - __Product Details__
        - __Large product image and product details__ allows user to see details of the product clearly.
        Users can read the full product description and again, select the products category to view more products in the same category.
        - __Quanity selector__ allows the user to increase/decrease the quantity of the product they wish to purchase. The 
        value cannot be set below 1 so no errors occur when the product is added to the bag.
        - __Add to bag button__ adds the product to the shopping bag.
        - __Success toasts__ when a product is added to the page a toast pops up letting the user know they have 
        successfully added the product to the bag and also allows them to view a summary of what is currently in their bag as 
        well as the total due excluding delivery, and what they need to spend to get free delivery. Clicking on the toast takes the 
        user to their shopping bag and allows them to continue with the purchase.
        - __Keep Shopping button__ Allows the user to return easily to the main products page.
    - __Edit/Add products__ these pages are only avaliable to superusers.
        - __Product Form__ consists of all fields required to create a new product. Category is selected through a drop down, containing 
        all categories. Edit form is prefilled with the product details so users can make edits quickly and easily.
        - __Product Image__ users are notified when uploading a new image what the file will be changed to, so users can see if a mistake is made
        When the user is editing a product the current product image is shown as a preview.

### Checkout page:
    - __Order Summary:__ Shows the user their shopping bag and a breakdown of their order, delivery and total costs, before they complete their purchase.
    - __Form__: Split into three sections, if any required fields are missed, the form cannot be submitted. Instead a popup appears at the missed field 
    reminding the user to fill it in before submitting again. 
        - The first contains the users information such as email and name. 
        - Delivery information is the next section. If the user is logged in they are able to save this information so next time they make 
        a purchase, this part of the form will be prefilled. 
        - Stripe payment is the last section where users enter their card details and can complete their purchase. The 
        form cannot be submitted if the credit card number is not valid, instead the page will reload, alerting them of the 
        issue.
    - __Loading overlay__: This is triggered when the form is submitted and shows the user their request is being processed. It consists of a 
    black transparent overlay and a spinning loading icon in site colours.

### Checkout Success page: 
    - __Success toast__ assures the user their order has been processed and gives them the order number and alerts them that they have 
    been sent a confirmation email. 
    - __Heading and intro__ thanks the user for their purchase and confirms the email their confirmation has been sent to.
    - __Order summary__ shows all the order details including the order number, date, products purchased, delivery information and 
    billing information.
    - __Back to shop or community buttons__ guides the user to other parts of the site they can explore.

### Community pages:

    - __Community page__ is avaliable for all users to view, however adding posts is restricted to authorised users.
        - __Search posts__: Users are able to search for posts using keywords they are interested in. Submitting the search will return
        all relevant posts and also display a reset button to allow them to return to the main view.
        - __Add Post button__: Avaliable at the top of the page so users can find it easily, takes the authenticated users to the add a post page
        and anonymous users to the login page.
        - __Posts__ consist of cards containing the post image, if it has one. The user who created it and a preview of the post so users can get an idea if it is 
        what they are looking for. The posts end with a button leading to the full post.
        - __Like and comment count__ On each post the number of likes and comments is also displayed so users know if there are comments to read 
        or whether or not the post is popular.
        - __Edit/Delete Buttons__ are only visible to the creator of the post, allowing them to remove or edit it. Delete post buttons are also 
        avaliable to superusers in order to allow them to regulate what is posted.

    - __Post detail page__ avaliable for all users to view, however adding comments or likes is 
    restricted to only authorised users.
        - __Post heading, image and body__: The heading is styled using the logo font. For posts with images, the image is displayed prominently and
        the full post is avaliable to read.
        - __Like button__: Shows the current number of likes. Allow logged in users to like or unlike a post which triggers a page reload with a toast notifying the user 
        that their like has been added and the like count will also increase.
        - __Comment button__:When pressed, by an authenticated user, toggles a collapsible at the bottom of the page with the comment form so the user can add a post.
        - __Comments__: Show the user posting the comment in different colours, depending on if they are a superuser, the post creator or a general user. 
            - __Edit/Delete buttons__ are avaliable to the creators of comments. The edit button produces the comment form prefilled and allows the user to make 
            and adjustment. The delete comment button is also avaliable to superusers to allow them to regulate comments.
        
    - __Add/Edit a post page__ is displayed simply with the logo font used for the heading and the pattern border page decoration.
        - __Post Form__ cannot be submitted without being fully filled in. The name of the file image chosen for the post is displayed once 
        one is selected. Edit form is prefilled for each of adjustment and a pop up toast appears, alerting the user that they are editing
        their post.

### Profile page:

     - Only avaliable when a user is authorised.
     - __User Profile Form__ allows a user to add/adjust their default shipping information to make checkout faster and easier.
     - __Order Summary__ is originally hidden when the page is loaded. Allows the user to bring up a summary of their previous orders 
     as well as select an order to view it's confirmation and full details.
     - __Liked Posts__ are orginially hidden when the page loads. Allows a user to view the heading of their liked posts so they can return to them easily, they are also able to 
     remove the like and therefore the post from their profile.

MEDIA : 
MAIN BORDER USED<a href="https://www.freepik.com/vectors/frame">Frame vector created by pch.vector - www.freepik.com</a>
LINK FOR SHOP BUTTON HENNA CONE : https://bluelotushenna.com/product/henna-cone-regular-1-oz/
LINK FOR BORDER: Image by <a href="https://pixabay.com/users/gdj-1086657/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3166177">Gordon Johnson</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3166177">Pixabay</a>
HOME IMAGE: https://www.salongold.co.uk/wp-content/uploads/2019/04/henna-art-1920x1080.jpg