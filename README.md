<a name="readme-top"></a>
<!--
Citation for this README:
https://github.com/othneildrew/Best-README-Template#readme
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/uva-cs3240-f22/project-a-27">
    <img src="#" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Group A-27: CavCourses/New Lous List</h3>

  <p align="center">
    A website for browsing classes, creating class schedules, and viewing friends' schedules. Created for CS 3240: Advanced Software Development in a group project.
    <br />
    <a href="https://cavcourses.herokuapp.com/"><strong>See our app! »</strong></a>
    <br />
    <br />
    <a href="https://github.com/megkuo/cavcourses">Project Page</a>
    ·
    <a href="https://f22.cs3240.org/lutherslist.html">Luther's List API</a>
    ·
    <a href="https://louslist.org/">Original Lous List</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
      <ul>
        <li><a href="#my-contributions">My Contributions</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is for the University of Virginia's CS 3240 (Advanced Software Development) course. Our team chose to build a Web App modeling the University of Virginia's beloved <a href="https://louslist.org/">Lous List</a>.

Here are the project-specific requirements we implemented:
* Students must be able to view and search classes, separated into logical categories (ex. by department).
* Students must be able to save a prospective schedule for a given semester. The system should prevent time conflicts and prevent signing up for multiple sections of the same course.
* Students should be able to “friend” other students to see their schedule and leave a comment on their schedule.

Here are the general project requirements:
* All projects must incorporate Google user accounts as the primary way that someone logs into the system.
* All users must have an account of some kind where they can store their personal information relevant to the app.
* All users must be able to maintain a list of “friends” in the app, where they can view key information about the other user. See the project options for details.
* All projects must incorporate the SIS / Class Listing API that we will provide, which will contain (mostly) up-to-date data from SIS that mirrors what you would currently see from Lou’s List.
* All projects must be built using the prescribed language (Python 3), framework (Django 4), build environment (GitHub Actions CI), source control management (GitHub), and cloud hosting (Heroku).
* You must use the PostgreSQL database engine for production on Heroku and continuous integration (on GitHub Actions).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. 


* Django
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### My Contributions

Here is a description of what I contributed to this project as the Scrum Master of my group:

Technical Contributions:
* Integrated Google Login via Google Cloud API/Django-allauth
* Revamped the schedules feature so that classes would display in the correct chronological order on the correct days, and would also fill the grid for the exact duration of the class (ex. a 50 minute class doesn't take up the whole hour/row on the schedule)
* Added avatars for users' accounts
* Created the header for the website using Bootstrap
* Helped to integrate team members' code, ex. updating the code for the advanced search to utilize data stored in the database, rather than pulling from the Luther's List API each time
* Added the comments feature to schedules

Interpersonal Contributions:
* Organized group meetings, oordinated distribution of responsibilities for each 2-week sprint, maintained communication within the group and with course staff
* Ensured we fulfilled all necessary requirements


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* Megan Kuo           - mlk6une@virginia.edu (Scrum Master)
* Connor Wilson       - crw8eg@virginia.edu  (DevOps)
* Srini Chelimilla    - slc8kf@virginia.edu  (UIUX)
* Johnny Lindsey      - jbl5xq@virginia.edu  (Requirements)
* Nathaniel Hershel   - nth5pdk@virginia.edu (Testing)

Project Link: [https://github.com/uva-cs3240-f22/project-a-27](https://github.com/uva-cs3240-f22/project-a-27)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thank you to the CS 3240 Staff for helping us accomplish this project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
[djangoproject.com]: #
[Django-url]: https://www.djangoproject.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[product-screenshot]: https://www.virginia.edu/sites/default/files/201904-sunset.jpg
![image](https://user-images.githubusercontent.com/83975442/206331274-d01c67ed-16ac-456f-987b-076f7cf723cd.png)
