# Cool Coders

[Link to deployed site](https://automarket-2a9033a7b561.herokuapp.com/)

<hr>
Cool Coders is your go-to hub for all things tech, offering a wealth of insightful posts on coding, industry trends, gadgets and more. Engage with a global community by favoriting posts, leaving comments, and sparking discussions. Share your own tech experiences through user-generated posts. Join Cool Coders today and immerse yourself in the dynamic world of technology.

![CoolCoders Image](./assets/readme-images/main-image.PNG)

# Table Of Content

- [User Experience](#user-experience)
- [Site Goals](#site-goals)
- [User Stories](#user-stories)
- [Scope](#scope)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Database Schema](#Database-Schema)
  - [Fonts](#Fonts)
  - [Wireframes](#Wireframes)
  - [Agile Methodology](#Agile-Methodology)
    - [Overview](#overview)
    - [EPICS(Milestones)](#epicsmilestones)
    - [User Stories issues](#user-stories-issues)
    - [MoSCoW prioritization](#moscow-prioritization)
    - [GitHub Projects](#github-projects)
- [Features](#features)
  - [Navbar](#Navbar)
  - [Footer](#Footer)
  - [Home](#Home)
    - [Hero Section](#hero-section)
    - [Search Form](#search-form)
    - [Recent Listings](#recent-listings)
    - [Listing Card](#listing-card)
  - [Listings Page](#listings-page)
  - [Create Listing](#create-listing)
  - [Profile Page](#profile-page)
  - [My Listings](#my-listings)
  - [My Favourites](#my-favourites)
  - [Remove From Favourites](#remove-from-favourites)
  - [Edit Listing](#edit-listing)
  - [Delete Listing](#delete-listing)
  - [View Listing](#view-listing)
  - [User account and User account listings](#user-account-and-user-account-listings)
  - [Sign In Page](#sign-in-page)
  - [Sign Up Page](#sign-up-page)
  - [Sign Out Confirmation](#sign-out-confirmation)
  - [Edit Profile](#edit-profile)
  - [Delete Profile Confirmation](#delete-profile-confirmation)
  - [We are sorry to see you go](#we-are-sorry-to-see-you-go)
  - [Password reset](#password-reset)
  - [Password reset email sent](#password-reset-email-sent)
  - [Enter a new password](#enter-a-new-password)
  - [Password Reset Completed](#password-reset-completed)
  - [Error Pages](#error-pages)
- [Future Features](#future-features)
- [Testing](#testing)
- [Bugs](#Bugs)
- [Technologies And Languages](#technologies-and-languages)
  - [Languages Used](#languages-used)
  - [Python Modules](#python-modules)
  - [Technologies and programs](#technologies-and-programs)
- [Deployment](#deployment)
  - [Before Deployment](#before-deployment)
  - [Deployment on Heroku](#deployment-on-heroku)
  - [Creating A Fork](#creating-a-fork)
  - [Cloning Repository](#cloning-repository)
- [Credits](#credits)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)
  - [Comments](#comments)

## User Experience

### User Stories

#### New User

- As a new user, I want to easily navigate and explore the Cool Coders platform to discover interesting tech topics.
- As a new user, I want to clearly understand the purpose of the website and its content so I can decided whether I wish to browse further.
- As a new user, I want to create a user profile and customize it with a short description of myself.
- As a new user, I want to contribute my own tech-related insights and experiences by writing posts to share with the community.
- As a new user, I want to be able filter content by category so I can quickly find the topics I am interested in.

#### Existing User

- As an existing user, I want to continue exploring new and exciting tech topics on Cool Coders to stay updated on the latest trends, popular posts and editors choices.
- As an existing user, I aim to regularly interact with the community by commenting on posts and actively participating in discussions.
- As an existing user I want to see my posts analytics such as engagement, likes and comments on a profile dashboard
- As an existing user I want to be able to update my information, password and biography and delete my account.
- As a existing user, I want to engage with the community by leaving comments on posts, asking questions, and participating in discussions.
- As a existing user, I want to read my favorite posts that resonate with me, building my own collection of tech resources.
- As a existing user, I to be able to edit or delete my posts and remove comments from other peoples articles.

#### Website Owner/Developer

- As a developer, I have the capability to establish a fresh Django project, facilitating the creation of the project's framework.
- As a developer, I possess the ability to establish connections to databases and media storage, ensuring the secure and successful storage of user data.
- As A developer, I will initiate the early deployment of the application, enabling me to validate the initial setup's functionality and continue testing throughout the development process.
- As the owner of the website, I have the authority to review and approve comments and posts submitted by users, ensuring that the content aligns with our community guidelines and maintains a respectful and constructive tone.
- As the owner of the website, such as banning users, when their behavior or content violates our terms of service or community standards, safeguarding the platform's integrity and creating a safe environment for all users.
- As the owner of the website I have complete control of the storage of data on an admin panel and and perform all CRUD applications available through the admin portal.

### Site Goals

1. Foster a thriving global tech community
2. Share and discuss the latest tech trends and insights
3. Create a platform for users to contribute their tech knowledge
4. Encourage collaboration and knowledge exchange
5. Connect tech enthusiasts from all backgrounds and expertise levels
6. Promote a love for coding and technology exploration

### Scope

The project's scope is to create and maintain "Cool Coders," an online platform dedicated to tech enthusiasts. Cool Coders will serve as a user-friendly and responsive space for individuals to explore, share, and interact with tech-related content. The platform will encompass the following key features:

1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. Responsive Design:

- The website will be responsive, allowing users to access it on both desktop and mobile devices.

3. User Authentication:

- Account registration is available for users, granting them full access to coolcoders features.
- Once registered, users can log in to access their profiles, posts, comments, and favourited items.

4. Profile Management:

- Authenticated users can update their username, fullname and biography
- Users can update their passwords when logged in
- Users can delete their profiles and all associated comments/posts.

5. Post Management:

- Users can create, update, read and delete their posts.
- Users can view all their posts from the profile page and by using the navigation functionalities.
- Posts will provide an image and a short excerpt description of the content.
- Users can view all other users posts from their profile pages.

6. Pagination:

- Pagination will be implemented on the category pages when post listings are more than 6.

7. Favorites:

- Authenticated users can view all their favourited posts from the profile page.
- Users can like and unlike posts to add them to their favourite from the post detail.

8. Notification Messages:

- Users will be notified with messages when posting, updating and deleting commets or posts as well as when logging in or out or signing up.

Benefits:

1. Prioritizing User Needs: The platform places the user's requirements at the forefront, streamlining the browsing experience, available posts creation and user communication on such posts.
2. Streamlined and Easy Navigation: Users can effortlessly move through various website sections, ensuring convenient and hassle-free access. This is performed by using the category selector, related posts sidebar and browsing user profiles.
3. User Analytics: Users gain valuable insights, allowing them to track and monitor metrics like the number of posts created, comments made, likes received, and favorites accumulated, enhancing their understanding of their contributions and interactions on Cool Coders.

## Design

### Colour Scheme

The website adopts a soothing and polished color scheme, mirroring the iconic colors of the MacBook Pro. These are black, light gray and white. This palette creates an overall professional and user-friendly ambiance, utilizing subtle variations in shade and transparency to direct user attention and elevate the website's visual allure. A hint of glassmorphism can be scene on article cards to futher the illusion of browsing on a tech item.

![Colour Scheme](./assets/readme-images/colour-palette.PNG)

### Database Schema

![database schema](./assets/readme-images/database-schema.png)

### Models

#### Allauth User Model

The User model is an integral component of Django Allauth, featuring pre-established fields as part of its standard configuration. Among these fields are username, email, name, password, and others. This model primarily serves the purpose of user authentication, which is why it is not recommended to make direct alterations to it. Furthermore, the User model is linked to the Profile model through a one-to-one relationship, facilitating the management of user-specific data and interactions.

#### Profile Model

Profile Model: The Profile Model provides a snapshot of each user's presence on the platform, encapsulating their information, activities, and preferences. It often includes fields for user-specific data such as name, bio and slug. It is has a one to one relationship with the auth User Model

#### Category Model

The Category Model categorizes and organizes posts, ensuring users can easily discover and explore tech topics. It typically includes fields for category name, description, and associations with posts to facilitate content organization and navigation within the platform.

#### Post Model

The Post Model is the core of the content creation process, where users share their tech-related knowledge, experiences, and insights. This model includes fields for post content, author, publication date, category association, and engagement metrics such as likes.

#### Comment Model

The Comment Model serves as the foundation for user engagement on the platform, allowing users to interact with posts by sharing their thoughts and feedback. It includes fields for the comment content, author, timestamp, and a foreign key relationship to associated posts.

### Fonts

The font used in this project is Roboto Slab, which compliments the design of the website. <br>
![Font](./assets/readme-images/font.PNG)

### Wireframes

- Home
  ![Home](./assets/readme-images/wireframes/Home.png)
- Listings
  ![listings](./assets/readme-images/wireframes/Listings.png)
- Single listing
  ![single-listing](./assets/readme-images/wireframes/single-listing.png)
- Log in
  ![login](./assets/readme-images/wireframes/login.png)
- My Listings
  ![my listings](./assets/readme-images/wireframes/my-listings.png)
- Profile
  ![profile](./assets/readme-images/wireframes/profile.png)

### Agile Methodology

#### Overview

This project was created using agile principles. This was a big learning curve together with my very first full-stack project. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### EPICS(Milestones)

In the context of the Agile methodology, the user stories are categorized into eight EPICS or Milestones. An extra Milestone named "Project Backlog" has been established to oversee any supplementary features, bugs, or tasks that might emerge throughout the development process.
![Milestones](./assets/readme-images/agile-milestones.PNG)

#### User Stories issues

The user story issue format comprises the user story itself, along with acceptance criteria and tasks delineating the necessary steps for resolving the issue. Whenever feasible, during development, commit messages are linked to their associated issues. This ensure each commits relevance as well as displaying the progress on each project issue. These issues are tracked with milestones/kanban and other agile tools.

#### MoSCoW prioritization

The "MoSCoW" technique was employed to efficiently sort and rank the project's features and demands according to their significance. "MoSCoW" represents "Must have, Should have, Could have, and Won't have," with each classification aiding in the organization and ranking of features. This method serves as a guiding principle for the development process, guaranteeing that the most essential elements are tackled as a priority.
![User Story](./assets/readme-images/user-story-moscow.PNG)

#### GitHub Projects/Kanban

A fundamental Kanban Board structure was employed to establish the project, which was segmented into columns like Todo, In Progress, Done, and Backlog. This configuration offered a transparent and well-structured method for monitoring task progress, facilitating the visualization and control of the workflow during the development process.
![User Story](./assets/readme-images/github-projects.PNG)

## Features

### Navbar

The navigation bar is a consistent element across all pages, designed using Bootstrap and optimized for full responsiveness. The left is centered around navigation of content while the right hand side is related to user authentication. Authenticated users can also see create post and view profile links while unauthenticated users only see a prompt to login/register.

The mobile version of the navbar has all the content rendered when a hamburger icon is clicked. When clicked a dropdown display is rendered showing all navigation links.

![nav logged out](./assets/readme-images/features/nav-logged-out.PNG)
![nav logged in](./assets/readme-images/features/nav-logged-in.PNG)
![nav mobile](./assets/readme-images/features/nav-mobile.PNG)

### Footer

The footer is a miniinmalist footer designed to link users to cool coders social links. The link are only for educational purposes as just link to the social platforms base url.
![Footer](./assets/readme-images/features/footer.PNG)

### Home

The Home Hero Section on Cool Coders features carefully curated tech-related content with three components: Popular Posts, highlighting articles with active user comments; Trending Posts, showcasing popular content based on user likes; and Editor's Choice, handpicked by the editorial team. Each post is displayed as a card with a link to the full article, accompanied by engagement metrics like comments and likes. Users can also access the author's profile, promoting community interaction and enhancing the user experience. Additionally, tag links are displayed to showcase posts from various categories, further enhancing content discovery.
![Home section](./assets/readme-images/features/nav-mobile.PNG)

### Category Page

The Category Page on Cool Coders is a dedicated space where users can explore a comprehensive collection of articles grouped by specific tech-related categories. Each category page is thoughtfully organized, presenting users with a wealth of content tailored to their interests. The articles are neatly paginated, with up to six articles displayed per page for easy navigation and efficient content browsing. This design allows users to delve deeply into the topics that intrigue them most, making it a valuable resource for in-depth exploration of various tech-related subjects within the Cool Coders community.
![Search Form](./assets/readme-images/features/home-search.PNG)

#### Article Card

The Article Card on Cool Coders is a concise yet informative snapshot of a user's post within a specific tech-related category. It includes the following key elements:

1. Author Profile: A visual representation of the author's profile picture and username, providing a quick way to identify the content creator.
2. Likes: The number of likes the post has received, offering a sense of its popularity and engagement.
3. Comments: The count of comments on the post, indicating the level of community discussion and interaction.
4. Category: Clearly indicating the tech category to which the post belongs, helping users quickly identify the content's subject matter.
5. Post Date: The date when the article was published, offering a reference for the recency of the content.
6. Title: The headline of the post, serving as a captivating entry point to the article's content.
7. Excerpt: A brief summary or excerpt from the article, providing users with a glimpse of the post's key points and enticing them to read further.

Together, these elements create a Category Card that is both visually appealing and informative, allowing users to make informed choices about which posts to explore further within a specific category.

![Listing Card](./assets/readme-images/features/listing-card.PNG)

### Post Detail Page

The Post Detail Page on Cool Coders is an immersive experience designed to provide users with in-depth access to an article's content and foster engagement. Here's what users can expect on this page:

1. Article Content: The central focus of the page is the article itself. Users can read the full content of the post, gaining insights into the topic, industry trends, or tech-related experiences shared by the author.
2. Comments Section: A dedicated comments section accompanies the article, displaying all user-generated comments related to the post. Users can participate in discussions, share their thoughts, and engage with the Cool Coders community by leaving comments or replies.
3. Comment Form: Below the comments section, a user-friendly comment form is readily available. Users can easily contribute to the conversation by typing and submitting their comments, which will appear alongside existing discussions.
4. Popular Posts in Category: To encourage further exploration within the same category, the page also showcases a selection of popular posts from the related category. This feature helps users discover additional relevant content, offering a seamless navigation experience.

The Post Detail Page serves as a hub for knowledge sharing and community interaction, ensuring that users not only have access to insightful content but can also actively engage, discuss, and explore more related posts within the category.
![Listings Page](./assets/readme-images/features/listing-results.PNG)

### Profile Page

The Profile Page on Cool Coders is an essential space for users to showcase their tech passions and contributions while also gaining insights into their own engagement within the community. Here's what you'll find on a user's profile:

#### Profile Info

1. Username, First Name and Last Name: Users' first and last names, adding a personal touch to their profiles.
2. Bio: A brief bio or description, allowing users to share more about themselves, their interests, or their professional background.
3. Email Address: The user's contact information, enabling communication with other community members.
4. Member Since:The date the user joined Cool Coders, providing a sense of their tenure within the community.

#### Post Info

1. Total Posts: The cumulative number of posts by the user.
2. Total Likes: The cumulative number of likes received by the user across all their posts, reflecting their content's popularity.
3. Total Comments: The overall count of comments made on the user's posts, indicating engagement and interaction with their content.
4. Total Favourites: The cumulative number of favourited posts of the user.

If the user is viewing their own profile, they have the ability to edit their posts and profile information, ensuring their profile remains up-to-date and their posts are well-maintained.
Users can also access their list of favorited posts, making it convenient to revisit their favorite content.

The Profile Page serves as an information-rich hub, where users can introduce themselves, showcase their contributions, and gain insights into their impact within the Cool Coders community. It fosters a sense of belonging and encourages active participation while enabling users to manage their own content and profile details.
![My Profile](./assets/readme-images/features/my-profile.PNG)

#### Toggle Favourites

The "Toggle Favorites" button allows authenticated users to quickly add or remove articles from their favorites, tailoring their content preferences with ease.
![Remove my favourites](./assets/readme-images/features/remove-favourites.PNG)

#### Edit Post

The "Edit Post" button empowers users to make quick updates to their published articles, ensuring they can keep their content current and accurate. The redirects users to the post article but only if they are authenticated and the post author.

![Edit Listing](./assets/readme-images/features/edit-listing.PNG)

#### Delete Post

The Delete Post button is visible to the post author only, enabling them to remove their own articles when needed. This feature grants users full control over their content, ensuring a personalized and streamlined experience. A confirmation modal is presented to warn users of their action.

![delete Listing](./assets/readme-images/features/delete-listing.PNG)

### Add/Edit Post Page

The Add/Edit Post Page on Cool Coders is a versatile platform that empowers users to craft and refine their tech-related articles with ease. Here's what this feature offers:

1. Create and Edit Articles: Users can compose new articles or edit existing ones, maintaining control over their content and insights.
2. Title: A clear and captivating title helps users convey the article's main theme, attracting readers and providing a structured entry point.
3. Content: The page provides a dedicated space for users to input the full content of their articles, allowing for in-depth exploration of tech topics.
4. Excerpt: Users can include a concise and engaging excerpt that provides a preview of the article's key points, enticing readers to delve further.
5. Image: The option to upload an image enhances visual appeal and adds context to the article, creating a more engaging reading experience.
   6.Category: Users can assign their articles to specific tech-related categories, ensuring they are appropriately classified and easily discoverable by others.
6. Delete Post Button (Edit Mode): In edit mode, users have the ability to delete their posts using a dedicated "Delete Post" button, granting full control over their content's management.

The Add/Edit Post Page is a user-friendly tool designed to facilitate content creation and refinement, enabling users to share their tech insights and knowledge within the Cool Coders community.

### Edit Profile Page

The Edit User Profile Page on Cool Coders is a user-centric feature that empowers users to manage and customize their personal information seamlessly. Here's what this page offers:

1. Edit User Profile Information: Users can conveniently update their First Name, Last Name, Username, Email, and Bio, ensuring that their profile accurately reflects their identity and interests.
   2.Password Change: This feature allows users to modify their password, enhancing account security and ensuring they maintain control over their login credentials.
2. Account Deletion: For those who choose to do so, the option to delete their account is available, allowing users to exercise control over their Cool Coders membership. Users will be prompted to confirm their action with a modal popup.

The Edit User Profile Page ensures a personalized and adaptable user experience, enabling individuals to make changes to their profile and account settings as needed while prioritizing their data security and personalization options.

![Gallery](./assets/readme-images/features/gallery.PNG)
Below that a description of the listing can be found. On the right side of the listing is where the most important information is presented to the user in a user-friendly manner.
The listing's title (consisting of the car make and car model) followed by the price and then how long ago was this listing created.
Below that the relevant specifications are displayed, and by using icons the information is visually structured better.
If the user visits a listing that is not theirs there is a heart that they can click to save the listing into their favourites the action is clearly communicated with a flash message and the heart changing to a red heart. If the user clicks the heart again, they will remove the listing from favourites and will get a flash message letting them know that.

![add favourites](./assets/readme-images/features/save-favourites.PNG)

![remove favourites](./assets/readme-images/features/saved-listing.PNG)

Further down there is a card with the seller's details, consisting of their image, name, email, phone, and location if added. Their image is a link to their user account page. Below that is an email seller button which when clicked opens a modal with a form. The form is prepopulated with the user's details if they are authenticated. Once submitted, an email is sent to the listing's owner with the details within the form.
![contact form](./assets/readme-images/features/contact-form.PNG)
![contact email](./assets/readme-images/features/contact-email.PNG)

### Sign Up page

This page comprises a form with fields for entering a username and password. Beneath the form is the sign up button which submits the form. Below the form is a redirect to the register page if the user does not have an account. Click the remember me checkbox to remain logged in as a session.
![Sign Up](./assets/readme-images/features/sign-in.PNG)

### Sign In page

It features a form with fields for inputting name, email, username, password, and password confirmation. Underneath the form, there is a link to log in for users with existing accounts, followed by the signup button. After signup, users receive a welcome email at the provided email address and are then directed to the profile page update form, where they can personalize their profiles.
![Sign In](./assets/readme-images/features/signup.PNG)

### Sign out page

Upon clicking the "log out" link in the navigation, users are directed to a confirmation page. This page includes a cautionary message and two buttons: one for returning and one for logging out.
![log out confirmation](./assets/readme-images/features/log-out-confirmation.PNG)

### Notification Messages

Notification messages were user every time the user performs CRUD operation, sign in, and sign out.

![messages](./assets/readme-images/features/flash-messages.PNG)

### Error Pages

1. 400 Error Page: The 400 error page is shown when there's a bad request or a user error, indicating that the request cannot be processed due to incorrect or invalid input.
2. 404 Error Page: This page is displayed when a user attempts to access a non-existent or unavailable resource, notifying them that the requested page cannot be found.
3. 403 Error Page: When a user tries to access a page or resource without the necessary permissions, the 403 error page is presented, indicating that access is forbidden.
4. 500 Error Page: This page appears when the server encounters an internal error, alerting the user that there's a problem with the website's server, and they should try again later.

## Future Features

1. I would like to include an API that can check the reg plate of a vehicle and get all the data for that vehicle. This way the users won't have to fill a very long form and it will improve the overall user experience.
2. I would like to update the database with car models for the Irish market. The models currently loaded are for the USA market.
3. I would like to expand the application by adding inbox feature and the option for the users to send and reply to messages.
4.

## Testing

Testing documentation can be found [here.](./TESTING.md)

## Bugs

| Bug                                                                                                                                                            | Status |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| [BUG: Deployment error #30](https://github.com/Dayana-N/AutoMarket-PP4/issues/30#issue-1816808909)                                                             | Closed |
| [BUG: Update user profile form images #33](https://github.com/Dayana-N/AutoMarket-PP4/issues/33#issue-1848255025)                                              | Closed |
| [BUG: Create listing form not displaying correctly #34](https://github.com/Dayana-N/AutoMarket-PP4/issues/34#issue-1857900988)                                 | Closed |
| [BUG: Error when the user deletes their default image #37](https://github.com/Dayana-N/AutoMarket-PP4/issues/37#issue-1867812729)                              | Closed |
| [BUG: Wrong time since on listings #38](https://github.com/Dayana-N/AutoMarket-PP4/issues/38#issue-1868276351)                                                 | Closed |
| [BUG: Page error when the user tries to delete their profile #39](https://github.com/Dayana-N/AutoMarket-PP4/issues/39#issue-1868283130)                       | Closed |
| [BUG: Issue when sending email to listing owner #40](https://github.com/Dayana-N/AutoMarket-PP4/issues/40#issue-1868292453)                                    | Closed |
| [BUG: Search results pagination #41](https://github.com/Dayana-N/AutoMarket-PP4/issues/41#issue-1868485937)                                                    | Closed |
| [BUG: Dynamic update on profile page causes issue when redirected back to the page #42](https://github.com/Dayana-N/AutoMarket-PP4/issues/42#issue-1868626287) | Open   |

## Technologies And Languages

### Languages Used

- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django
- Django Rest Framework

### Python Modules

- Boto3 is the Amazon Web Services (AWS) SDK for Python. It allows to interact with AWS services, such as S3

- dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

- django-resized - This package provides utilities for resizing images in Django.

- django-storages - Django Storages is a collection of custom storage backends for Django, including support for storing files on remote services like AWS S3.

- django-widget-tweaks - Django Widget Tweaks is a package that simplifies working with form widgets and templates in Djang

- djangorestframework - Django REST framework is a toolkit for building Web APIs in Django.

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

- s3transfer - S3 Transfer is a library for managing file transfers to and from Amazon S3 storage.

- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.
- django humanize - A set of Django template filters useful for adding a “human touch” to data. Used to transform large numbers into easy to read numbers

### Technologies and programs

- [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon
- [Lightbox](https://lokeshdhakar.com/projects/lightbox2/) was used to display the listings images in a more user friendly way
- [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as a starting point for the project.
- [Photoshop](https://www.adobe.com/ie/products/photoshop.html) was used for creating the mockup images of the website during planning stage.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Online Convert](https://image.online-convert.com/convert-to-webp) used to convert images to webp format
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [Box Shadow Generator](https://cssgenerator.org/box-shadow-css-generator.html) was used to generate the shadows

## Deployment

### Before Deployment

To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.
- Then commit and push the changes to GitHub.

! Before pushing code to GitHub ensure all credentials are in an env.py file, which is included in the .gitignore file. This tells Git not to track this file which will prevent it from being added to Github and the credentials being exposed.

### Deployment on Heroku

- To deploy the project on Heroku, first create an account.
- Once logged in, create a new app by clicking on the create app button
- Pick a unique name for the app, select a region, and click Create App.
- On the next page select the settings tab and scroll down to Config Vars. If there are any files that should be hidden like credentials and API keys they should be added here. In this project, there are credentials that need to be protected. This project requires credentials added for:

1. Django's secret key
2. Database Credentials
3. AWS access key
4. AWS secret key
5. Email host password.

- Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python
- From the tab above select the deploy section.
- The deployment method for this project is GitHub. Once selected, confirm that we want to connect to GitHub, search for the repository name, and click connect to connect the Heroku app to our GitHub code.
- Scroll further down to the deploy section where automatic deploys can be enabled, which means that the app will update every time code is pushed to GitHub. Click deploy and wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed with a view button to see the app.

### Creating a fork

1. Navigate to the [repository](https://github.com/Dayana-N/AutoMarket-PP4)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description
4. Choose to copy only the main branch or all branches to the new fork.
5. Click Create a Fork. A repository should appear in your GitHub

### Cloning Repository

1. Navigate to the [repository](https://github.com/Dayana-N/AutoMarket-PP4)
2. Click on the Code button on top of the repository and copy the link.
3. Open Git Bash and change the working directory to the location where you want the cloned directory.
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

## Credits

### Media

- [Default user image](https://res.cloudinary.com/dpmykpsih/image/upload/c_fill,f_auto,q_auto,w_360/tj-samson-site-251/media/5c7a249a36974d978322f386269f9c24.jpg)
- [Hero image](https://static1.hotcarsimages.com/wordpress/wp-content/uploads/2023/01/2023-bmw-4-series-coupe-featured.jpg)
- [Sorry to see you go image](https://charatoon.com/?id=5214)
- [Default Listing Image](https://png.pngtree.com/template/20220419/ourmid/pngtree-photo-coming-soon-abstract-admin-banner-image_1262901.jpg)
- The images for the listing were taken from [https://www.autotrader.co.uk/](https://www.autotrader.co.uk/). They are for display purpose only.

### Code

- Learned how to setup django project and deploy to Heroku from CI Django Blog walkthrough
- [How to create dependant drop down](https://github.com/akjasim/cb_dj_dependent_dropdown) The code was later refactored to use Django Rest Api
- [The Car models list is from (back4app)](https://www.back4app.com/database/back4app/car-make-model-dataset)
- [How to use Q objects for complex queries](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html)
- [Pagination fix for multiple search parameters](https://stackoverflow.com/questions/46026268/pagination-and-get-parameters)
- [How to catch email sending exceptions](https://stackoverflow.com/questions/41457565/how-to-catch-email-sending-exceptions-in-django-1-10)
- The search form was inspired visually by Brad Traversy's Python course
- How to setup AWS - CI instructions from the PP5 walkthrough
- I learned how to use advanced Django concepts like signals, sending emails, how to use Django rest framework, and more from Dennis[ Ivy's Django course](https://dennisivy.teachable.com/p/django-beginners-course)

### Acknowledgements

- Huge thank you to my mentor Ronan McClelland for encouraging me to go with my very ambitious idea for my first full-stack project.
- The Slack community and especially Indrek who listened to my struggles during development.
- Dennis Ivy for the brilliant 18-hour Django course, which explains in detail a lot of the main Django concepts.

### Comments

This project consists of three apps - API, Listings, and Users.
The User's app handles everything related to the users including their listings and favourites since they are directly related to the user.
The Listings app handles everything related to the listings including CRUD functionality and add and remove from favourites.
The API app was created to serialize the data and pass it to the front end. In particular the car models. On the front end, JavaScript makes a call to fetch all the models based on the user's selection of car make.
The car makes and models were loaded into the database by calling a function in the utils.py file. The code loops over all of the car models in the cars dictionary and uploads them to the database. This function should not be called otherwise. It has been left there to document the process.

I wanted to include some automated testing, but unfortunately i ran out of time. However, this is something I plan to add in the future to help me manage the project as I keep adding more features.

This project is particularly close to my heart, not only because it's my very first full-stack project but also because it's inspired by my love for cars.
