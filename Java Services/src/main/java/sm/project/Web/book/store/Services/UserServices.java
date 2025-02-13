/**
 * This class represents the User Service.
 * It provides methods for handling user-related operations such as retrieval,
 * authentication, and creation.
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

 package sm.project.Web.book.store.Services;

 import java.util.Optional;
 import org.springframework.beans.factory.annotation.Autowired;
 import org.springframework.stereotype.Service;
 import sm.project.Web.book.store.Repositories.UserRepositories;
 import sm.project.Web.book.store.data_objects.AuthDTO;
 import sm.project.Web.book.store.data_objects.UserDAO;
 
 /**
  * Service class for managing user-related operations.
  */
 @Service
 public class UserServices {
     
     @Autowired
     public UserRepositories userRepositories;
 
     /**
      * Retrieves a user by their unique identifier.
      *
      * @param id The unique identifier of the user.
      * @return An Optional containing the user if found, otherwise empty.
      */
     public Optional<UserDAO> getById(int id) {
         if (id < 0) {
             return Optional.empty();
         }
         return userRepositories.getById(id);
     }
 
     /**
      * Authenticates a user based on their username and password.
      *
      * @param authData The authentication data containing username and password.
      * @return An Optional containing the authenticated user if credentials match, otherwise empty.
      */
     public Optional<UserDAO> login(AuthDTO authData) {
         if (authData.getPassword() == null || authData.getUsername() == null) {
             return Optional.empty();
         }
         return userRepositories.login(authData);
     }
 
     /**
      * Creates a new user and adds them to the repository.
      *
      * @param user The user data to be stored.
      * @return The newly created user, or null if required fields are missing.
      */
     public UserDAO create(UserDAO user) {
         if (user.name == null || user.nickname == null || user.password == null || user.email == null) {
             return null;
         }
         return userRepositories.create(user);
     }
 }
 