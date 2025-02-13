/**
 * This class represents the User Repository.
 * It provides methods for managing user data within the application,
 * including retrieval, authentication, and creation.
 *
 * Author: Melisa Melenge <cmmaldonadom@udistrital.edu.co>
 *
 * This file is part of sm.project.Web.book.store.
 *
 * sm.project.Web.book.store is free software: you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or any later version.
 *
 * sm.project.Web.book.store is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with sm.project.Web.book.store. If not, see <https://www.gnu.org/licenses/>.
 */

 package sm.project.Web.book.store.Repositories;

 import java.io.InputStream;
 import java.nio.charset.StandardCharsets;
 import java.io.IOException;
 import java.io.FileNotFoundException;
 import org.springframework.stereotype.Repository;
 import jakarta.annotation.PostConstruct;
 import sm.project.Web.book.store.data_objects.*;
 import java.util.Optional;
 import java.util.ArrayList;
 import java.util.List;
 import org.json.JSONArray;
 import org.json.JSONObject;
 
 /**
  * Repository class for managing user data.
  */
 @Repository
 public class UserRepositories {
     private List<UserDAO> users = new ArrayList<UserDAO>();
 
     /**
      * Initializes the repository by loading user data from a JSON file.
      */
     @PostConstruct
     public void init() {
         this.loadData();
     }
 
     /**
      * Loads user data from a JSON file located at "data/users.json".
      */
     private void loadData() {
         String path = "data/users.json";
         try (InputStream is = getClass().getClassLoader().getResourceAsStream(path)) {
             if (is == null) {
                 throw new FileNotFoundException("File not found " + path);
             }
             String content = new String(is.readAllBytes(), StandardCharsets.UTF_8);
             JSONArray jsonArray = new JSONArray(content);
             for (int i = 0; i < jsonArray.length(); i++) {
                 JSONObject jsonObject = jsonArray.getJSONObject(i);
                 UserDAO user = new UserDAO(
                     jsonObject.getInt("id"),
                     jsonObject.getString("name"),
                     jsonObject.getString("nickname"),
                     jsonObject.getString("password"),
                     jsonObject.getString("email")
                 );
                 users.add(user);
             }
         } catch (IOException e) {
             e.printStackTrace();
         }
     }
 
     /**
      * Retrieves a user by their unique identifier.
      *
      * @param id The unique identifier of the user.
      * @return An Optional containing the user if found, otherwise empty.
      */
     public Optional<UserDAO> getById(int id) {
         for (UserDAO user : this.users) {
             if (user.id == id) {
                 return Optional.of(user);
             }
         }
         return Optional.empty();
     }
 
     /**
      * Authenticates a user based on their username and password.
      *
      * @param authData The authentication data containing username and password.
      * @return An Optional containing the authenticated user if credentials match, otherwise empty.
      */
     public Optional<UserDAO> login(AuthDTO authData) {
         for (UserDAO user : this.users) {
             if (user.nickname.equals(authData.getUsername()) && user.password.equals(authData.getPassword())) {
                 return Optional.of(user);
             }
         }
         return Optional.empty();
     }
 
     /**
      * Creates a new user with a unique ID and adds them to the repository.
      *
      * @param user The user data to be stored.
      * @return The newly created user.
      */
     public UserDAO create(UserDAO user) {
         int lastId = -1;
         for (UserDAO user_ : this.users) {
             if (user.id > lastId) {
                 lastId = user.id;
             }
         }
         lastId += 1;
 
         UserDAO newUser = new UserDAO(
             lastId,
             user.name,
             user.nickname,
             user.password,
             user.email
         );
         this.users.add(newUser);
         return newUser;
     }
 }
 