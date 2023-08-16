# 0x0E. SQL - More queries

## Author's name: *Pearl Chimelumeze Udoka.*
---
# This project consists of tasks such as;
* **0. My privileges!** - Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`). - `0-privileges.sql`.
* **1. Root user** - Write a script that creates the MySQL server user `user_0d_1`. - `1-create_user.sql`.
* **2. Read user** - Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`. - `2-create_read_user.sql`.
* **3. Always a name** - Write a script that creates the table `force_name` on your MySQL server. - `3-force_name.sql`.
* **4. ID can't be null** - Write a script that creates the table `id_not_null` on your MySQL server. - `4-never_empty.sql`.
* **5. Unique ID** - Write a script that creates the table `unique_id` on your MySQL server. - `5-unique_id.sql`.
* **6. States table** - Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server. - `6-states.sql`.
* **7. Cities table** - Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server. - `7-cities.sql`.
* **8. Cities of California** - Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`. - `8-cities_of_california_subquery.sql`.
* **9. Cities by States** - Write a script that lists all cities contained in the database `hbtn_0d_usa`. - `9-cities_by_state_join.sql`.
* **10. Genre ID by show** - Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql). Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. - `10-genre_id_by_show.sql`.
* **11. Genre ID for all shows** - Write a script that lists all shows contained in the database `hbtn_0d_tvshows`. - `11-genre_id_all_shows.sql`.
* **12. No genre** - Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked. - `12-no_genre.sql`.
* **13. Number of shows by genre** - Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each. Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`. - `13-count_shows_by_genre.sql`.
* **14. My genres** - Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`. - `14-my_genres.sql`.
* **15. Only Comedy** - Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`. - `15-comedy_only.sql`.
* **16. List shows and genres** - Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title` - `tv_genres.name`. - `16-shows_by_genre.sql`.
* **17. Not my genre** - Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`. - `100-not_my_genres.sql`.
* **18. No Comedy tonight!** - Write a script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`. - `101-not_a_comedy.sql`.
* **19. Rotten tomatoes** - Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql). Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating. - `102-rating_shows.sql`.
* **20. Best genre** - Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating. - `103-rating_genres.sql`.
