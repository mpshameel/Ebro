/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.1.32-community : Database - supermarket
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`supermarket` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `supermarket`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `Category_Name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`id`,`Category_Name`) values (1,'Vegitable'),(2,'Fruit'),(3,'Cosmetics'),(4,'Snaks'),(5,'frozen'),(6,'Nuts'),(7,'Cool Drinks'),(8,'samplesa'),(9,'Electronics'),(10,'sample.'),(11,'null'),(12,'null'),(13,'null'),(14,'samp'),(15,'null'),(16,'null');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `Pr.NO` int(10) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(100) DEFAULT NULL,
  `pro_name` varchar(100) DEFAULT NULL,
  `Quantity` int(100) DEFAULT NULL,
  `Price` int(100) DEFAULT NULL,
  PRIMARY KEY (`Pr.NO`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`Pr.NO`,`cat_name`,`pro_name`,`Quantity`,`Price`) values (1,'null',NULL,NULL,NULL),(2,'Vegitable',NULL,NULL,NULL),(3,'Vegitable',NULL,NULL,NULL),(4,'Cosmetics',NULL,NULL,NULL),(5,'Fruit','apple',2,200),(6,'Snaks','sammusa',1,50);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
