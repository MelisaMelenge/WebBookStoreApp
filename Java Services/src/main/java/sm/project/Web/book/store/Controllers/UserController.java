/**
 * This module defines the user controller within the application.
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

 package sm.project.Web.book.store.Controllers;

 import java.util.Optional;

 import org.springframework.beans.factory.annotation.Autowired;
 import org.springframework.web.bind.annotation.GetMapping;
 import org.springframework.web.bind.annotation.PathVariable;
 import org.springframework.web.bind.annotation.PostMapping;
 import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import sm.project.Web.book.store.Services.UserServices;
import sm.project.Web.book.store.data_objects.AuthDTO;
import sm.project.Web.book.store.data_objects.UserDAO;
 
 /**
  * REST controller that manages user-related operations.
  */
 @RestController
 @RequestMapping("v1/users")
 public class UserController {
     @Autowired
     private UserServices userServices;
 
     /**
      * Retrieves a user by their ID.
      *
      * @param id User identifier.
      * @return An Optional object containing the user if found.
      */
     @GetMapping("/get_by_id/{idUser}")
     public Optional<UserDAO> getById(@PathVariable("idUser") int id) {
         return userServices.getById(id);
     }
 
     /**
      * Authenticates a user with the provided credentials.
      *
      * @param authData Authentication data.
      * @return An Optional object containing the authenticated user if credentials are correct.
      */
     @PostMapping("/login")
     public Optional<UserDAO> login(@RequestBody AuthDTO authData) {
         return userServices.login(authData);
     }
 
     /**
      * Creates a new user in the database.
      *
      * @param user Object containing the new user's data.
      * @return The created user.
      */
     @PostMapping("/create")
     public UserDAO create(@RequestBody UserDAO user) {
         return userServices.create(user);
     }
 }