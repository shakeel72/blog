-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 13, 2020 at 12:00 PM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blogging`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog_comment`
--

DROP TABLE IF EXISTS `blog_comment`;
CREATE TABLE IF NOT EXISTS `blog_comment` (
  `blog_id` varchar(25) NOT NULL,
  `comments` text NOT NULL,
  `approved_reject` varchar(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blog_comment`
--

INSERT INTO `blog_comment` (`blog_id`, `comments`, `approved_reject`) VALUES
('BlogId', 'Comments', 'Yes'),
('Blovfknxv', 'Commdvkjdcbx hjvc', '');

-- --------------------------------------------------------

--
-- Table structure for table `blog_table`
--

DROP TABLE IF EXISTS `blog_table`;
CREATE TABLE IF NOT EXISTS `blog_table` (
  `blog_id` varchar(15) NOT NULL,
  `blog_name` varchar(25) NOT NULL,
  `blog_description` text NOT NULL,
  `blog_comment` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blog_table`
--

INSERT INTO `blog_table` (`blog_id`, `blog_name`, `blog_description`, `blog_comment`) VALUES
('BlogId', 'Name', 'Description_of_blog_message', 'Comments');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
