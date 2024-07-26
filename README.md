Rentex Project Documentation
Project Overview
Rentex is a Django project designed to manage and rent various categories of items. The project includes several categories and modules for user management, item rentals, and other functionalities.

Categories
Cameras
Trekking Gear
Riding Gear
Action Cameras
Gaming Consoles
Winter Wear
Audio-Visual Equipment
Camping Gear
Creator Gear
Project Structure
1. Profile Management
The Profile module handles user profile management and includes the following sections:

Profile Overview: Displays general profile information.
My Wallet: Manages the user's wallet, including balance and transaction history.
My Account: Handles user account settings and personal information.
My Orders: Shows the history of orders placed by the user.
My Cart: Manages items currently in the user's shopping cart.
2. Renting
The Rent module is dedicated to managing rental items. Users can browse available rental options, view details, and make bookings.

Cameras
Trekking Gear
Riding Gear
Action Cameras
Gaming Consoles
Winter Wear
Audio-Visual Equipment
Camping Gear
Creator Gear
3. Refurbished
Displays refurbished items available for rent or purchase.

4. Policies and FAQs
Policies: Provides details about rental policies, terms, and conditions.
FAQs: Answers frequently asked questions about the rental process and policies.
Navigation
Sidebar
The sidebar provides easy access to various sections of the site:

Home: Link to the home page.
Profile: Dropdown menu with links to:
Profile Overview
My Wallet
My Account
My Orders
My Cart
Logout
Rent: Dropdown menu with links to various rental categories:
Cameras
Trekking Gear
Riding Gear
Action Cameras
Gaming Consoles
Winter Wear
Audio-Visual Equipment
Camping Gear
Creator Gear
Refurbished: Link to refurbished items.
Policies: Link to the policies section.
FAQs: Link to the FAQs section.
Main Navigation Bar
The main navigation bar includes:

Home
Rent: Dropdown with links to rental categories.
Refurbished
Policies
FAQs
Search Bar: Allows users to search for rental items or information.
App Modules
1. Profile App
Handles user profile management with views for overview, wallet, account settings, orders, and cart.

2. Rent App
Manages rental items and user interactions with the rental system.

3. Refurbished App
Displays refurbished items available for rent or purchase.

4. Policies App
Provides information about rental policies and terms of service.

5. FAQs App
Answers common questions related to the rental process and policies.

Templates
The project uses a base template base.html which includes the navigation bar and sidebar. Other templates extend this base template to include specific content for each section of the site.

base.html
The base.html template includes:

Sidebar navigation with links and icons.
Main content area where specific page content is rendered.
Footer with copyright information.
home.html
Displays the home page content. Extends base.html.

Rent Section Templates
rent/cameras_list.html: Displays a list of cameras available for rent.
rent/cameras_detail.html: Shows details for a specific camera.
rent/cameras_form.html: Form for creating or updating camera information.
rent/cameras_confirm_delete.html: Confirmation page for deleting a camera.
(Similar templates for other categories)
Static Files
Static files such as CSS and JavaScript are managed to ensure proper styling and functionality of the project's frontend.

CSS
styles.css: Custom styles for the project.
JavaScript
scripts.js: Custom scripts for functionality.
CRUD Operations
Trekking Gear
List View: Displays a list of trekking gear items.
Detail View: Shows details for a specific trekking gear item.
Create View: Form for adding new trekking gear.
Update View: Form for editing existing trekking gear.
Delete View: Confirmation page for deleting trekking gear.
Camera, Riding Gear, Action Camera, Gaming Console, Winter Wear, Audio-Visual Equipment, Camping Gear, Creator Gear
Similar CRUD operations as Trekking Gear: List, Detail, Create, Update, and Delete views for each category.