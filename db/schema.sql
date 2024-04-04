-- auto-generated definition
create table users
(
    seq       integer     not null
        primary key autoincrement,
    name      varchar(64) not null,
    create_by varchar(64) not null,
    create_at datetime    not null,
    update_by varchar(64) not null,
    update_at datetime    not null
);

-- auto-generated definition
create table labels
(
    seq       integer      not null
        primary key autoincrement,
    labels    varchar(256) not null,
    create_at datetime     not null,
    user_seq  bigint       not null
);

create index labels_user_seq_fbbf0e0c
    on labels (user_seq);

-- auto-generated definition
create table contacts
(
    seq          integer      not null
        primary key autoincrement,
    name         varchar(256) not null,
    image_url    varchar(256),
    email        varchar(256) not null,
    phone_number varchar(256) not null,
    address      varchar(256),
    web_site     varchar(256),
    company      varchar(256),
    position     varchar(256),
    birthday     datetime,
    memo         varchar(1000),
    create_by    varchar(64)  not null,
    create_at    datetime     not null,
    update_by    varchar(64)  not null,
    update_at    datetime     not null,
    user_seq     bigint       not null
);

create index contacts_user_seq_575f19a2
    on contacts (user_seq);

-- auto-generated definition
create table contact_labels
(
    seq         integer not null
        primary key autoincrement,
    contact_seq bigint  not null,
    label_seq   bigint  not null
);

create index contact_labels_contact_seq_45cd6089
    on contact_labels (contact_seq);

create index contact_labels_label_seq_e636441a
    on contact_labels (label_seq);

