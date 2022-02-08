drop database if exists test_sql;
create database test_sql;
use test_sql;

create table product (
    id int primary key auto_increment,
    name varchar(50) not null,
    price float not null check (price >= 0),
    description varchar(200)
);

create table `order` (
    id int primary key auto_increment,
    email varchar(50) not null,
    product int not null,
    foreign key (product) references product(id)
)
