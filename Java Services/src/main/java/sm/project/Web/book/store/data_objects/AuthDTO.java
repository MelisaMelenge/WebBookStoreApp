/**
 * This class represents the authentication data transfer object (DTO).
 * It is used to transfer authentication credentials within the application.
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

 package sm.project.Web.book.store.data_objects;

 /**
  * Data Transfer Object (DTO) for user authentication.
  */
 public class AuthDTO {
     private String username;
     private String password;
 
     /**
      * Constructs an AuthDTO with the provided username and password.
      *
      * @param username The username of the user.
      * @param password The user's password.
      */
     public AuthDTO(String username, String password) {
         this.username = username;
         this.password = password;
     }
 
     public String getUsername() {
         return username;
     }

     public String getPassword() {
         return password;
     }
 }