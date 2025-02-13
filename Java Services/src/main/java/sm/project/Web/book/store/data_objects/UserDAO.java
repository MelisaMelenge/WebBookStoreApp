/**
 * This class represents the User Data Access Object (DAO).
 * It is used to manage user data within the application.
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
  * Data Access Object (DAO) for user information.
  */
 public class UserDAO {
     public int id;
     public String name;
     public String nickname;
     public String password;
     public String email;
 
     /**
      * Constructs a UserDAO with the provided user details.
      *
      * @param id The unique identifier of the user.
      * @param name The full name of the user.
      * @param nickname The nickname of the user.
      * @param password The user's password.
      * @param email The email address of the user.
      */
     public UserDAO(int id, String name, String nickname, String password, String email) {
         this.id = id;
         this.name = name;
         this.nickname = nickname;
         this.password = password;
         this.email = email;
     }
 }