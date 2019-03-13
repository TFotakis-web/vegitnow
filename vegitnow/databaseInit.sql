INSERT INTO "general_language" ("Name", "Code") VALUES ('English', 'en');
INSERT INTO "general_language" ("Name", "Code") VALUES ('Ελληνικά', 'gr');
INSERT INTO "articles_articletype" ("Name", "Language_id") VALUES ('Recipe', 1);
INSERT INTO "articles_articletype" ("Name", "Language_id") VALUES ('Article', 2);
INSERT INTO "articles_articletypenametranslation" ("Name", "ArticleType_id", "Language_id") VALUES ('Συνταγή', 1, 2);
INSERT INTO "articles_articletypenametranslation" ("Name", "ArticleType_id", "Language_id") VALUES ('Άρθρο', 2, 2);
