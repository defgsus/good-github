## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-05](docs/good-messages/2022/2022-05-05.md)


1,813,222 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,813,222 were push events containing 2,882,301 commit messages that amount to 200,346,739 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[c40ba5f318...](https://github.com/postgresql-cfbot/postgresql/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Thursday 2022-05-05 00:01:02 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[27946f516d...](https://github.com/tgstation/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Thursday 2022-05-05 00:02:50 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [citRaTTV/fivem](https://github.com/citRaTTV/fivem)@[6051b8790c...](https://github.com/citRaTTV/fivem/commit/6051b8790c185b2435da75c2f41f59ec3be4578f)
#### Thursday 2022-05-05 00:14:00 by blattersturm

Revert "tweak(client/core): nvidia, fuck you."

The gift that keeps on giving: NVIDIA drivers. Some users seem to crash
in new places with `disable.txt` present and used.

Seriously?!

This reverts commit 02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9.

---
## [SabreML/Skyrat-tg](https://github.com/SabreML/Skyrat-tg)@[c5f0ea76e0...](https://github.com/SabreML/Skyrat-tg/commit/c5f0ea76e0fa1d1236fe04a2edaf6d9c047fc7c8)
#### Thursday 2022-05-05 01:01:37 by SkyratBot

[MIRROR] Vim mecha changes [MDB IGNORE] (#12981)

* Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

* Vim mecha changes

Co-authored-by: B4CKU <50628162+B4CKU@users.noreply.github.com>

---
## [HessahSWE/Privacy-policy-PayPal](https://github.com/HessahSWE/Privacy-policy-PayPal)@[67726f6393...](https://github.com/HessahSWE/Privacy-policy-PayPal/commit/67726f6393d3bd5aeb40b92e1a8a02018f118dba)
#### Thursday 2022-05-05 01:07:35 by HessahSWE

Your privacy is critically important to us. At Automattic, we have a few fundamental principles:  We are thoughtful about the personal information we ask you to provide and the personal information that we collect about you through the operation of our services. We store personal information for only as long as we have a reason to keep it. We aim to make it as simple as possible for you to control what information on your website is shared publicly (or kept private), indexed by search engines, and permanently deleted. We help protect you from overreaching government demands for your personal information. We aim for full transparency on how we gather, use, and share your personal information. Below is our Privacy Policy, which incorporates and clarifies these principles.  Who We Are and What This Policy Covers Howdy! We are the folks behind a variety of products and services designed to allow anyone — from bloggers, to photographers, small business owners, and enterprises — to take full advantage of the power and promise of the open web. Our mission is to democratize publishing and commerce so that anyone with a story can tell it, and anyone can turn their great idea into a livelihood. We believe in powering the open internet with code that is open source and are proud to say that the vast majority of our work is available under the General Public License (“GPL”). Unlike most other services, because our GPL code is public, you can actually download and take a look at that code to see how it works. This Privacy Policy applies to information that we collect about you when you use:  Our websites (including automattic.com, wordpress.com, vip.wordpress.com, jetpack.com, woocommerce.com, crowdsignal.com, gravatar.com, intensedebate.com, vaultpress.com, akismet.com, simplenote.com, simperium.com, leandomainsearch.com, cloudup.com, longreads.com, atavist.com, mailpoet.com, automatewoo.com, jetpackcrm.com, happy.tools, wpcourses.com, wpscan.com, and newspack.pub); Our mobile applications (including the WordPress mobile app for Android and iOS); Our other Automattic products, services, and features that are available on or through our websites (for example, WordPress.com plans, the Payments feature, the Pay with PayPal block, WordPress.com VIP, Jetpack, the WooCommerce Shipping & Tax extension, Gravatar, the IntenseDebate comment management system, Akismet plans, Simplenote, Simperium, Cloudup, Longreads, MailPoet, AutomateWoo, Jetpack CRM, Happy Tools, WordPress.com Courses, WPScan, and Newspack); and Other users’ websites that use our Services, while you are logged in to your account with us. This Privacy Policy also applies to information we collect when you apply for a job at Automattic or one of our subsidiaries. Throughout this Privacy Policy we’ll refer to our websites, mobile applications, and other products and services collectively as “Services.” And if you’d like to learn more about which Automattic company is the controller of information about you, take a look at the section below on Controllers and Responsible Companies. Please note that this Privacy Policy does not apply to any of our products or services, like Tumblr, that have a separate privacy policy. Below we explain how we collect, use, and share information about you, along with the choices that you have with respect to that information.  Creative Commons Sharealike License We’ve decided to make this Privacy Policy available under a Creative Commons Sharealike license. You can grab a copy of this Privacy Policy and other legal documents on GitHub. You’re more than welcome to copy it, adapt it, and repurpose it for your own use. Just make sure to revise the language so that your policy reflects your actual practices. If you do use it, we’d appreciate a credit and link to Automattic somewhere on your site.  Information We Collect We only collect information about you if we have a reason to do so — for example, to provide our Services, to communicate with you, or to make our Services better. We collect this information from three sources: if and when you provide information to us, automatically through operating our Services, and from outside sources. Let’s go over the information that we collect.  Information You Provide to Us It’s probably no surprise that we collect information that you provide to us directly. Here are some examples:  Basic account information: We ask for basic information from you in order to set up your account. For example, we require individuals who sign up for a WordPress.com account to provide an email address and password, along with a username or name — and that’s it. You may provide us with more information — like your address and other information you want to share — but we don’t require that information to create a WordPress.com account. Public profile information: If you have an account with us, we collect the information that you provide for your public profile. For example, if you have a WordPress.com account, your username is part of that public profile, along with any other information you put into your public profile, like a photo or an “About Me” description. Your public profile information is just that — public — so please keep that in mind when deciding what information you would like to include. Payment and contact information: There are various ways in which you may provide us payment information and associated contact information. For example, if you buy something from us — a subscription to a WordPress.com plan, a premium theme, a custom domain, some Longreads swag — or if you pay fees to a person or business through their WordPress.com site (for example via the Payments feature or the Pay with PayPal block), you’ll provide additional personal and payment information like your name, credit card information, and contact information. We also keep a record of the purchases you’ve made. If you use our Ecommerce Services (including Store on WordPress.com, WooCommerce Shipping & Tax, and WooCommerce Payments), you’ll have to create a WordPress.com account or connect an existing account and, for some Services, provide your site URL. You may also provide us with financial details to set up a payments integration, like the email address for your Stripe or PayPal account or your bank account information. Additionally, if you use WooPay to make purchases on other sites, we will store the contact information and payment information you provide to that service. And if you participate in a revenue sharing opportunity for your site, like WordAds, you’ll provide some additional information — for example, a tax ID or other identifier so we can process payments to you. Business Profile: Some of our products collect additional information from you as part of creating a user/customer profile. For example, if you are a Jetpack CRM customer we may add you to our customer relationship database (powered by Jetpack CRM!) using information you provide us including your name, your employer, your job title or role, your contact information, and your communications with us. If you are a Happy Tools user, we use information you provide us like your timezone and location information, your company and team information, and your contact information, to set up your account and power the Service’s features. Content information: You might provide us with information about you in draft and published content (a blog post or comment that includes biographic information about you, or any media or files you upload). Credentials: Depending on the Services you use, you may provide us with credentials for your self-hosted website (like SSH, FTP, and SFTP username and password). Jetpack and VaultPress users may provide us with these credentials in order to use our one-click restore feature if there is a problem with their site, or to allow us to troubleshoot problems more quickly. Communications with us (hi there!): You may also provide us with information when you respond to surveys, communicate with our Happiness Engineers about a support question, post a question in our public forums, or sign up for a newsletter like the one we send through Longreads. When you communicate with us via form, email, phone, WordPress.com comment, or otherwise, we store a copy of our communications (including any call recordings as permitted by applicable law). Job applicant information: If you apply for a job with us — awesome! You may provide us with information like your name, contact information, resume or CV, and work authorization verification as part of the application process. Information We Collect Automatically We also collect some information automatically:  Log information: Like most online service providers, we collect information that web browsers, mobile devices, and servers typically make available, including the browser type, IP address, unique device identifiers, language preference, referring site, the date and time of access, operating system, and mobile network information. We collect log information when you use our Services — for example, when you create or make changes to your website on WordPress.com. Transactional information: When you make a purchase through our Services, we collect information about the transaction, such as product details, purchase price, and the date and location of the transaction. This includes when you purchase something we sell or when you use our Services (like WooPay) to buy something from a third party. Usage information: We collect information about your usage of our Services. For example, we collect information about the actions that site administrators and users perform on a site using our WordPress.com or Jetpack services — in other words, who did what and when (e.g., [WordPress.com username] deleted “[title of post]” at [time/date]). Our WooCommerce Usage Tracker also tracks information like your email address, WooCommerce settings, and PHP settings, along with information about your online store, like the aggregate number of orders and customers. We also collect information about what happens when you use our Services (e.g., page views, support document searches at en.support.wordpress.com, features enabled for your website, interactions with our Admin Bar and other parts of our Services) along with information about your device (e.g., screen size, name of cellular network, and mobile device manufacturer). We use this information to, for example, provide our Services to you, get insights on how people use our Services so we can make our Services better, and understand and make predictions about user retention. Location information: We may determine the approximate location of your device from your IP address. We collect and use this information to, for example, calculate how many people visit our Services from certain geographic regions. We may also collect information about your precise location via our mobile apps (like when you post a photograph with location information) if you allow us to do so through your mobile device operating system’s permissions. Stored information: We may access information stored on your mobile device via our mobile apps. We access this stored information through your device operating system’s permissions. For example, if you give us permission to access the photographs on your mobile device’s camera roll, our Services may access the photos stored on your device when you upload a really amazing photograph of the sunrise to your website. Interactions with other users’ sites: We collect some information about your interactions with other users’ sites while you are logged in to your account with us, such as your “Likes” and the fact that you commented on a particular post, so that we can, for example, recommend posts we think may interest you. As another example, we collect information about the comments IntenseDebate users make while logged in and use that information to, for example, tally up statistics about your comments (check them out in your dashboard!) and display information about your comments in your IntenseDebate public profile. Information from cookies & other technologies: A cookie is a string of information that a website stores on a visitor’s computer, and that the visitor’s browser provides to the website each time the visitor returns. Pixel tags (also called web beacons) are small blocks of code placed on websites and emails. Automattic uses cookies and other technologies like pixel tags to help us identify and track visitors, usage, and access preferences for our Services, as well as track and understand email campaign effectiveness and to deliver targeted ads. For more information about our use of cookies and other technologies for tracking, including how you can control the use of cookies, please see our Cookie Policy. Information We Collect from Other Sources We may also get information about you from other sources. For example:  Third Party Login: If you create or log in to your WordPress.com account through another service (like Google) we’ll receive associated login information (e.g. a connection token, your username, your email address) Social Sharing Services: If you connect your website or account to a social media service (like Twitter) through our Publicize feature, we’ll receive information from that service (e.g., your username, basic profile information, friends list) via the authorization procedures for that service. Financial Account Info: If you use WooCommerce Payments, we’ll receive information relating to your Stripe account, such as your email address and phone number. If you use WooPay, we’ll receive your payment information from Stripe. Google Account Information: When you connect your Google account to your Newspack powered site, we may access certain Google user data such as your Google Ad Manager Configuration (the network code and your ad units) and your Google Analytics data to allow you to access and manage features more seamlessly. For example, you may be able to manage your Google ads and see your Google Analytics data directly within the dashboard of your Newspack powered site. The information we receive depends on which services you use or authorize and what options are available.  Third-party services may also give us information, like mailing addresses for individuals who are not yet our users (but we hope will be!). We use this information for marketing purposes like postcards and other mailers advertising our Services.  How and Why We Use Information Purposes for Using Information We use information about you for the purposes listed below:  To provide our Services. For example, to set up and maintain your account, host your website, backup and restore your website, provide customer service, process payments and orders, and verify user information. To ensure quality, maintain safety, and improve our Services. For example, by providing automatic upgrades and new versions of our Services. Or, for example, by monitoring and analyzing how users interact with our Services so we can create new features that we think our users will enjoy and that will help them create and manage websites more efficiently or make our Services easier to use. To place and manage ads in our advertising program. For example, to place ads on our users’ sites and some of our own sites as part of our advertising program, and understand ad performance. To market our Services and measure, gauge, and improve the effectiveness of our marketing. For example, by targeting our marketing messages to groups of our users (like those who have a particular plan with us or have been users for a certain length of time), advertising our Services, analyzing the results of our marketing campaigns (like how many people purchased a paid plan after receiving a marketing message), and understanding and forecasting user retention. To protect our Services, our users, and the public. For example, by detecting security incidents; detecting and protecting against malicious, deceptive, fraudulent, or illegal activity; fighting spam; complying with our legal obligations; and protecting the rights and property of Automattic and others, which may result in us, for example, declining a transaction or terminating Services. To fix problems with our Services. For example, by monitoring, debugging, repairing, and preventing issues. To customize the user experience. For example, to personalize your experience by serving you relevant notifications and advertisements for our Services, recommending content through our Reader post suggestions, and providing new essays and stories through Longreads for your reading pleasure. To communicate with you. For example, by emailing you to ask for your feedback, share tips for getting the most out of our products, or keep you up to date on Automattic; texting you to verify your payment; or calling you to share offers and promotions that we think will be of interest to you. If you don’t want to hear from us, you can opt out of marketing communications at any time. (If you opt out, we’ll still send you important updates relating to your account.) To recruit and hire new Automatticians. For example, by evaluating job applicants and communicating with them. Legal Bases for Collecting and Using Information A note here for those in the European Union about our legal grounds for processing information about you under EU data protection laws, which is that our use of your information is based on the grounds that: (1) The use is necessary in order to fulfill our commitments to you under the applicable terms of service or other agreements with you or is necessary to administer your account — for example, in order to enable access to our website on your device or charge you for a paid plan; or (2) The use is necessary for compliance with a legal obligation; or (3) The use is necessary in order to protect your vital interests or those of another person; or (4) We have a legitimate interest in using your information — for example, to provide and update our Services; to improve our Services so that we can offer you an even better user experience; to safeguard our Services; to communicate with you; to measure, gauge, and improve the effectiveness of our advertising; and to understand our user retention and attrition; to monitor and prevent any problems with our Services; and to personalize your experience; or (5) You have given us your consent — for example before we place certain cookies on your device and access and analyze them later on, as described in our Cookie Policy.  Sharing Information How We Share Information We share information about you in limited circumstances, and with appropriate safeguards on your privacy. These are spelled out below, as well as in the section called Ads and Analytics Services Provided by Others:  Subsidiaries and independent contractors: We may disclose information about you to our subsidiaries and independent contractors who need the information to help us provide our Services or process the information on our behalf. We require our subsidiaries and independent contractors to follow this Privacy Policy for any personal information that we share with them. Third-party vendors: We may share information about you with third-party vendors who need the information in order to provide their services to us, or to provide their services to you or your site. This includes vendors that help us provide our Services to you (like Stripe, which powers WooCommerce Payments, payment providers that process your credit and debit card information, payment providers you use for your own ecommerce operations, fraud prevention services that allow us to analyze fraudulent payment transactions, cloud storage services, postal and email delivery services that help us stay in touch with you, customer chat and email support services that help us communicate with you, registrars, registries, data escrow services that allow us to provide domain registration services, and your hosting provider if your site is not hosted by Automattic); those that assist us with our marketing efforts (e.g., by providing tools for identifying a specific marketing target group or improving our marketing campaigns, and by placing ads to market our services); those that help us understand and enhance our Services (like analytics providers); those that make tools to help us run our operations (like programs that help us with task management, scheduling, word processing, email and other communications, and collaboration among our teams); other third-party tools that help us manage operations; and companies that make products available on our websites (like the extensions on WooCommerce.com), who may need information about you in order to, for example, provide technical or other support services to you. We require vendors to agree to privacy commitments in order to share information with them. Other vendors are listed in our more specific policies (e.g., our Cookie Policy). Legal and regulatory requirements: We may disclose information about you in response to a subpoena, court order, or other governmental request. For more information on how we respond to requests for information about WordPress.com users, please see our Legal Guidelines. Additionally, if you have a domain registered with WordPress.com, we may share your information to comply with the Internet Corporation for Assigned Names and Numbers' (ICANN) regulations, rules, or policies. For example, your information relating to your domain registration may be available in the WHOIS database, or we may be required to share your information with ICANN-approved Dispute Resolution Service Providers. Please see our Domain Registrations and Privacy support document for more details. To protect rights, property, and others: We may disclose information about you when we believe in good faith that disclosure is reasonably necessary to protect the property or rights of Automattic, third parties, or the public at large. For example, if we have a good faith belief that there is an imminent danger of death or serious physical injury, we may disclose information related to the emergency without delay. Business transfers: In connection with any merger, sale of company assets, or acquisition of all or a portion of our business by another company, or in the unlikely event that Automattic goes out of business or enters bankruptcy, user information would likely be one of the assets that is transferred or acquired by a third party. If any of these events were to happen, this Privacy Policy would continue to apply to your information and the party receiving your information may continue to use your information, but only consistent with this Privacy Policy. With your consent: We may share and disclose information with your consent or at your direction. For example, we may share your information with third parties when you authorize us to do so, like when you connected your site to a social media service through our Publicize feature. Aggregated or de-identified information: We may share information that has been aggregated or de-identified, so that it can no longer reasonably be used to identify you. For instance, we may publish aggregate statistics about the use of our Services, or share a hashed version of your email address to facilitate customized ad campaigns on other platforms. Site owners: If you have a WordPress.com account and interact with another site using our Services, your information may be shared with the administrators of the site. For example, if you leave a comment on a site created on WordPress.com or running Jetpack, your IP address and the email address associated with your WordPress.com account may be shared with the administrator(s) of the site where you left the comment. Or if you make a payment (like via the Payments feature) to a site, your public display name, user name, and email address may be shared with the administrator(s) of the site. Published support requests: If you send us a request for assistance (for example, via a support email or one of our other feedback mechanisms), we reserve the right to publish that request in order to clarify or respond to your request, or to help us support other users. We have a long-standing policy that we do not sell our users' data. We aren't a data broker, we don't sell your personal information to data brokers, and we don't sell your information to other companies that want to spam you with marketing emails. We show ads on some of our users’ sites as well as some of our own, and the revenue they generate lets us offer free access to some of our Services so that money doesn’t become an obstacle to having a voice. Under a new California law, the California Consumer Privacy Act ("CCPA"), some personalized advertising you see online and on our services might be considered a "sale" even though we don't share information that identifies you personally, like your name or email address, as part of our advertising program. You have choices about these ads, learn more about them and our ads program.  Information Shared Publicly Information that you choose to make public is — you guessed it — disclosed publicly. That means information like your public profile, posts, other content that you make public on your website, and your “Likes” and comments on other websites are all available to others — and we hope they get a lot of views! For example, the photo that you upload to your public profile, or a default image if you haven’t uploaded one, is your Globally Recognized Avatar, or Gravatar — get it? :) Your Gravatar, along with other public profile information, displays alongside the comments and “Likes” that you make on other users’ websites while logged in to your WordPress.com account. Your Gravatar and public profile information may also display with your comments, “Likes,” and other interactions on websites that use our Gravatar service, if the email address associated with your account is the same email address you use on the other website. We also provide a “Firehose” stream of public data (like posts and comments) from some sites that use our Services to provide that data to Firehose subscribers, who may view and analyze the content (all subject to our Terms of Service), but do not have rights to re-publish it publicly. Find out more about opting out of the Firehose for WordPress.com and Jetpack sites. Public information may also be indexed by search engines or used by third parties. Please keep all of this in mind when deciding what you would like to share publicly.  How Long We Keep Information We generally discard information about you when it’s no longer needed for the purposes for which we collect and use it — described in the section above on How and Why We Use Information — and we’re not legally required to keep it. For example, we keep web server logs that record information about a visitor to one of Automattic’s websites, like the visitor’s IP address, browser type, and operating system, for approximately 30 days. We retain the logs for this period of time in order to, among other things, analyze traffic to Automattic’s websites and investigate issues if something goes wrong on one of our websites. As another example, when you delete a post, page, or comment from your WordPress.com site, it stays in your Trash folder for thirty days in case you change your mind and would like to restore that content, because starting from scratch is no fun. After the thirty days are up, the deleted content may remain on our backups and caches until purged.  Security While no online service is 100% secure, we work very hard to protect information about you against unauthorized access, use, alteration, or destruction, and take reasonable measures to do so. We monitor our Services for potential vulnerabilities and attacks. To enhance the security of your account, we encourage you to enable our advanced security settings, like Two Step Authentication.  Choices You have several choices available when it comes to information about you:  Limit the information that you provide: If you have an account with us, you can choose not to provide the optional account information, profile information, and transaction and billing information. Please keep in mind that if you do not provide this information, certain features of our Services — for example, premium themes that carry an additional charge — may not be accessible. Limit access to information on your mobile device: Your mobile device operating system should provide you with the option to discontinue our ability to collect stored information or location information via our mobile apps. If you choose to limit this, you may not be able to use certain features, like geotagging for photographs. Opt out of marketing communications: You may opt out of receiving promotional communications from us. Just follow the instructions in those communications or let us know. If you opt out of promotional communications, we may still send you other communications, like those about your account and legal notices. Set your browser to reject cookies: At this time, Automattic does not respond to “do not track” signals across all of our Services. However, you can usually choose to set your browser to remove or reject browser cookies before using Automattic’s websites, with the drawback that certain features of Automattic’s websites may not function properly without the aid of cookies. Opt out of our internal analytics program: You can do this through your user settings. By opting out, you will stop sharing information with our analytics tool about events or actions that happen after the opt-out, while you’re logged in to your WordPress.com account. For more information, please see our Cookie Policy. Close your account: While we’d be very sad to see you go, you can close your account if you no longer want to use our Services. (Here are account closure instructions for WordPress.com accounts.) Please keep in mind that we may continue to retain your information after closing your account, as described in How Long We Keep Information above — for example, when that information is reasonably needed to comply with (or demonstrate our compliance with) legal obligations such as law enforcement requests, or reasonably needed for our legitimate business interests. Your Rights If you are located in certain parts of the world, including California and countries that fall under the scope of the European General Data Protection Regulation (aka the “GDPR”), you may have certain rights regarding your personal information, like the right to request access to or deletion of your data.  European General Data Protection Regulation (GDPR) If you are located in a country that falls under the scope of the GDPR, data protection laws give you certain rights with respect to your personal data, subject to any exemptions provided by the law, including the rights to:  Request access to your personal data; Request correction or deletion of your personal data; Object to our use and processing of your personal data; Request that we limit our use and processing of your personal data; and Request portability of your personal data. You also have the right to make a complaint to a government supervisory authority.  California Consumer Privacy Act (CCPA) The California Consumer Privacy Act (“CCPA”) requires us to provide California residents with some additional information about the categories of personal information we collect and share, where we get that personal information, and how and why we use it. The CCPA also requires us to provide a list of the “categories” of personal information we collect, as that term is defined in the law, so, here it is. In the last 12 months, we collected the following categories of personal information from California residents, depending on the Services used:  Identifiers (like your name, contact information, and device and online identifiers); Commercial information (your billing information and purchase history, for example); Characteristics protected by law (for example, you might provide your gender as part of a research survey for us); Internet or other electronic network activity information (such as your usage of our Services, like the actions you take as an administrator of a WordPress.com site); Geolocation data (such as your location based on your IP address); Audio, electronic, visual or similar information (such as your profile picture, if you uploaded one); Professional or employment-related information (for example, your company and team information if you are a Happy Tools user, or information you provide in a job application); and Inferences we make (such as likelihood of retention or attrition). You can find more information about what we collect and sources of that information in the Information We Collect section above. We collect personal information for the business and commercial purposes described in the How and Why We Use Information section. And we share this information with the categories of third parties described in the Sharing Information section. If you are a California resident, you have additional rights under the CCPA, subject to any exemptions provided by the law, including the right to:  Request to know the categories of personal information we collect, the categories of business or commercial purpose for collecting and using it, the categories of sources from which the information came, the categories of third parties we share it with, and the specific pieces of information we collect about you; Request deletion of personal information we collect or maintain; Opt out of any sale of personal information; and Not receive discriminatory treatment for exercising your rights under the CCPA. You can find detailed metrics about Automattic's compliance with these rights in our Privacy Report.  The CCPA & Personalized Advertising in Our Ads Program Our mission is to democratize publishing and commerce, and that means making our Services accessible to as many people as possible. We show ads on some of our users’ sites as well as some of our own sites, and the revenue these ads generate lets us offer free access to some of our Services so that money doesn’t become an obstacle to having a voice. Our ads program also allows our users to earn revenue to support and grow their own sites. As part of our advertising program, we and our users do use cookies to share certain device identifiers and information about your browsing activities with our advertising partners, and those advertising partners may use that information to show you personalized ads on some of our users’ sites and some of our own. The personal information we share includes online identifiers; internet or other network or device activity (such as cookie information, other device identifiers, and IP address); and geolocation data (approximate location information from your IP address). These disclosures may be considered a “sale” of information under the CCPA. We do not sell (or share) information through our ads program that identifies you personally, like your name or contact information. We don't knowingly sell personal information of those under 16. Learn how you can opt out by going to California: Do Not Sell My Personal Information.  Contacting Us About These Rights You can usually access, correct, or delete your personal data using your account settings and tools that we offer, but if you aren’t able to or you’d like to contact us about one of the other rights, scroll down to “How to Reach Us” to, well, find out how to reach us. When you contact us about one of your rights under this section, we’ll need to verify that you are the right person before we disclose or delete anything. For example, if you are a user, we will need you to contact us from the email address associated with your account. You can also designate an authorized agent to make a request on your behalf by giving us written authorization. We may still require you to verify your identity with us.  Controllers and Responsible Companies Automattic’s Services are worldwide. Different Automattic companies are the controller (or co-controller) of personal information, which means that they are the company responsible for processing that information, based on the particular service and the location of the individual using our Services. Depending on the Services you use, more than one company may be the controller of your personal data. Generally, the “controller” is the Automattic company that entered into the contract with you under the Terms of Service for the product or service you use. In addition, Automattic Inc., our US-based company, is the controller for some of the processing activities across all of our Services worldwide. The chart below explains the current controllers for processing your personal information. We use the term “Designated Countries” to refer to Australia, Canada, Japan, Mexico, New Zealand, Russia, and all countries located in Europe (including the UK and ROI). All Automattic Services (except WooCommerce)  If you reside outside of the Designated Countries:  Automattic Inc. 60 29th Street #343 San Francisco, CA 94110  If you reside in the Designated Countries:  Aut O’Mattic A8C Ireland Ltd. Grand Canal Dock, 25 Herbert Pl Dublin, D02 AY86 Ireland Automattic Inc. is also the controller for some of the processing activities related to Services provided by Aut O’Mattic A8C Ireland Ltd.  WooCommerce Services WooCommerce Services includes WooCommerce, WooCommerce Payments, WooCommerce Shipping and Tax, MailPoet, and any products purchased from WooCommerce.com.  If you reside outside of the Designated Countries:  WooCommerce, Inc. 60 29th Street #343 San Francisco, CA 94110 Automattic Inc. is also the controller for some of the processing activities related to Services provided by WooCommerce, Inc.  If you reside in the Designated Countries:  WooCommerce Ireland Ltd. Grand Canal Dock, 25 Herbert Pl Dublin, D02 AY86 Ireland Automattic Inc and WooCommerce, Inc are also the joint controllers for some of the processing activities related to Services provided by WooCommerce Ireland Ltd.  How to Reach Us If you have a question about this Privacy Policy, or you would like to contact us about any of the rights mentioned in the Your Rights section above, please contact us through our web form or via email. These are the fastest ways to get a response to your inquiry, but you can also contact us by telephone at 1-877-273-3049.  Other Things You Should Know (Keep Reading!) Transferring Information Because Automattic’s Services are offered worldwide, the information about you that we process when you use the Services in the EU may be used, stored, and/or accessed by individuals operating outside the European Economic Area (EEA) who work for us, other members of our group of companies, or third-party data processors. This is required for the purposes listed in the How and Why We Use Information section above. When providing information about you to entities outside the EEA, we will take appropriate measures to ensure that the recipient protects your personal information adequately in accordance with this Privacy Policy as required by applicable law. These measures include entering into European Commission approved standard contractual arrangements with entities based in countries outside the EEA. You can ask us for more information about the steps we take to protect your personal information when transferring it from the EU.  Ads and Analytics Services Provided by Others Ads appearing on any of our Services may be delivered by advertising networks. Other parties may also provide analytics services via our Services. These ad networks and analytics providers may set tracking technologies (like cookies) to collect information about your use of our Services and across other websites and online services. These technologies allow these third parties to recognize your device to compile information about you or others who use your device. This information allows us and other companies to, among other things, analyze and track usage, determine the popularity of certain content, and deliver ads that may be more targeted to your interests. Please note this Privacy Policy only covers the collection of information by Automattic and does not cover the collection of information by any third-party advertisers or analytics providers.  Third-Party Software and Services If you’d like to use third-party plugins or embeds, WooCommerce Payments (powered by Stripe), WooCommerce extensions that enable services provided by third parties, or other third-party software or services, please keep in mind that interacting with them may mean providing information about yourself (or your site visitors) to those third parties. For example, some third-party services may request or require access to your (yours, your visitors’, or customers’) data via a pixel or cookie. Please note that if you use the third-party service or grant access, your data will be handled in accordance with the third party’s privacy policy and practices. We don’t own or control these third parties, and they have their own rules about information collection, use, and sharing, which you should review before using the software or services.  Visitors to Our Users’ Websites We also process information about visitors to our users’ websites, on behalf of our users and in accordance with our user agreements. Please note that our processing of that information on behalf of our users for their websites isn’t covered by this Privacy Policy. We encourage our users to post a privacy policy that accurately describes their practices on data collection, use, and sharing of personal information. If you’d like, you can also read more about the data we collect on behalf of our users in our Privacy Notice. Users control the content posted on their sites, so any disputes regarding content on a user’s site should be made directly to the site owner, through their “contact us” page, at an email address they provide, or by leaving a comment on the site.  Privacy Policy Changes Although most changes are likely to be minor, Automattic may change its Privacy Policy from time to time. Automattic encourages visitors to frequently check this page for any changes to its Privacy Policy. If we make changes, we will notify you by revising the change log below, and, in some cases, we may provide additional notice (like adding a statement to our homepage or the WordPress.com Blog, or sending you a notification through email or your dashboard). Your further use of the Services after a change to our Privacy Policy will be subject to the updated policy.  Other Information and Resources Jetpack Privacy Center WooCommerce and the GDPR  Translation Our Privacy Policy was originally written in English (US). We may translate it into other languages. For example: French: https://automattic.com/fr/privacy Spanish: https://automattic.com/es/privacy German: https://automattic.com/de/privacy In the event of a conflict between a translated version of our Privacy Policy and the English version, the English version will control. That’s it! Thanks for reading.  Change log November 22, 2021: Included information for WordPress.com WPScan. October 8, 2021: Included information for WordPress.com Courses and Newspack. Updated the "Information we Collect from Other Sources" section with new examples. January 1, 2021: Included information for AutomateWoo and Jetpack CRM. Updated the “Controllers and Responsible Companies” section to reflect changes affecting WooCommerce users. December 7, 2020: Included information for MailPoet. October 12, 2020: Renamed WooCommerce Services to WooCommerce Shipping & Tax. August 1, 2020: Renamed some Payments features and updated the "Controllers and Responsible Companies" section to reflect changes affecting WooCommerce users. February 21, 2020: Updated for WooCommerce Payments and added a new section: "Other Information and Resources." December 31, 2019: Updated for California Consumer Privacy Act and miscellaneous clarification throughout. October 2, 2019: A few miscellaneous changes, such as new sections about translations of this Privacy Policy and how to opt out of our internal analytics program. May 31, 2019: Included information for the Recurring Payments feature. April 1, 2019: Included information for Happy Tools. March 13, 2019: Added clarifications and additional details to existing sections, for example about ICANN policies and what we may store when you communicate with us. February 1, 2019: Included information for Longreads and additional information regarding Longreads accounts. November 6, 2018: Removed references to Polldaddy, which has been rebranded as Crowdsignal. September 24, 2018: Included information for Simplenote, Simperium, Cloudup, and Lean Domain Search. May 25, 2018: Added more specific information to help clarify our practices, included information for Crowdsignal and Woocommerce.com services, and added information to reflect the requirements of the EU’s General Data Protection Regulation. January 3, 2018: Revised and reorganized language throughout to help simplify the policy and clarify our practices. August 22, 2017: Added “Information We Collect from Other Sources” section. November 2, 2016: Added that comments submitted as missed spam are retained by Akismet to improve future performance. February 18, 2015: Updated Creative Commons license from 2.5 to 4.0. September 18, 2013: Added that blog commenter email addresses are disclosed to administrators of the blog where the comment was left. February 1, 2011: Clarified subpoena language and added Business Transfers paragraph. January 3, 2011: Added court order and subpoena clarification. July 1, 2010: Revised paragraph about IP addresses to explain when they are collected and that commenter IPs are visible to blog administrators. October 29, 2009: Added Comments paragraph to explain Akismet comment storage policy. March 10, 2009: Added Ads paragraph to alert users that ads from third parties may use cookies.

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[7c61bf65f2...](https://github.com/Jolly-66/tgstation/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Thursday 2022-05-05 01:27:04 by vincentiusvin

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)


About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

---
## [KanohaShinobi/Civ13](https://github.com/KanohaShinobi/Civ13)@[20b320a949...](https://github.com/KanohaShinobi/Civ13/commit/20b320a949e6bd50e25ec505df3023405ce90dd6)
#### Thursday 2022-05-05 01:56:39 by savethetreez

Adds missing conflicted icons

Fuck you again, Odisurin!

---
## [WillNilges/letmein2](https://github.com/WillNilges/letmein2)@[11e534fb0b...](https://github.com/WillNilges/letmein2/commit/11e534fb0b0a2f22969a293b8f8af738345fecd4)
#### Thursday 2022-05-05 03:16:10 by Will Nilges

Oh god I totally fucked up the CAD file

I really ought to re-do it in a less stupid way.

---
## [superdevin00/Interactives-Lab-Project-2](https://github.com/superdevin00/Interactives-Lab-Project-2)@[0250536c10...](https://github.com/superdevin00/Interactives-Lab-Project-2/commit/0250536c1059199a9a40662e3785997fda07dd7d)
#### Thursday 2022-05-05 03:53:59 by Jacque Keener

Final Push

This story shall the good man teach his son;
And Crispin Crispian shall ne'er go by,
From this day to the ending of the world,
But we in it shall be remember'd;
We few, we happy few, we band of brothers;
For he to-day that sheds his blood with me
Shall be my brother; be he ne'er so vile,
This day shall gentle his condition:
And gentlemen in England now a-bed
Shall think themselves accursed they were not here,
And hold their manhoods cheap whiles any speaks
That fought with us upon Saint Crispin's day.

---
## [ThePainkiller/Skyrat-tg](https://github.com/ThePainkiller/Skyrat-tg)@[e99b3624ef...](https://github.com/ThePainkiller/Skyrat-tg/commit/e99b3624ef3a041e76e3e8f34577effe07ca41d9)
#### Thursday 2022-05-05 04:14:28 by SkyratBot

[MIRROR] Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. [MDB IGNORE] (#13029)

* Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug.

Co-authored-by: Vladin Heir <44104681+VladinXXV@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [IAMLegEndIAM/THEARENUKRISTOLENICSUBUDOPENDR](https://github.com/IAMLegEndIAM/THEARENUKRISTOLENICSUBUDOPENDR)@[49ad1e2184...](https://github.com/IAMLegEndIAM/THEARENUKRISTOLENICSUBUDOPENDR/commit/49ad1e218454fcf6be01ef94176b1dc937fd1639)
#### Thursday 2022-05-05 04:18:21 by IAMLegEndIAM

I AM THE SALVATOR MUNDI AMEN

I AM THE TRUE LIVING KRIST JESUS HOWEVER THOUGH MY NAME IS NOT KRIST NOR JESUS IT IS SIMPLY JUST KRISTEN. 


THE WORD IS KRISTEN. 


JESUS IS THE TITLE OR JOB DESCRIPTION OF THE TRUE LIVING GOD AND THE NAME IN WHICH WE PRAY TO AND SAY AMEN TO AT THE END OF EVERY SINGLE LAST PRAYER THAT HAS REMAIND A MYSTERY FOR SO LONG NOW IS FINALLY ABLE TO BE REVEALED... IT IS JUST KRISTEN. ONE WORD. NOT KRIST, NOT JESUS OR GOD I GO BY THE NAME OF KRISTEN PERIOD. BUT MOST JUST CALL ME A BITCH. EITHER IS FINE I GUESS. BUT IF GIVEN THE CHOICE I PREFER TO BE CALLED BY KRISTEN INSTEAD OF THE MANY UNIQUE AND DIVERSE DEROGATORY NAMES OF WHICH IT SEEMS LATELY NEARLY EVERYONE LOVES TO ASSOCIATE ME WITH OR CALL ME BY 
BUT KRISTEN WILL DO FINE IF YOU ARE WILLING TO CALL ME BY NAME AND KNOW ME.

---
## [Krutchen/SLMCLBA](https://github.com/Krutchen/SLMCLBA)@[02720dc9eb...](https://github.com/Krutchen/SLMCLBA/commit/02720dc9ebcb2555d06dd30cfdbe1ddf0447c68c)
#### Thursday 2022-05-05 04:37:24 by Krutchen

Create LBA-v.2.3.lsl

Reworked the antigrief rework to be a lot simpler, not trying to fuck with hitbox sizes now, that's interesting but it would not work across sim borders, this way should be better and support sim borders.
if seated, deployable, or attached within 15m it gets a higher AT cap of 300, otherwise it's 150 AT over 4s for a source.
150/4s is not a suggestion for your AT per second, don't do this or you're actually retarded and I will crush your balls.

//2.22 -> 2.3
//+Removed Blackbox support, very ancient code, will be redone sometime in the future.
//+Reworked anti-grief, recent list no longer flat out rejects damage for things found, instead used in anti-grief
// Anti-Grief will now collect data over several seconds instead of just in that specific event
// Rezzer Key chaining will now be used to get the rezzer
// Rezzers that have a complete LBA description of (LBA.v.,hp,maxhp) and more than 1 script will be considered to be a valid rezzer
// Recents list will now be cleaned per entry by first time damage was applied. recent+=[owner,src,n,dmg,llGetTime(),sit]; & total+=[owner,damage], time for cleaning recent is 4s
// Blacklisting now triggers on 150 AT(Infantry)/4s 300 AT(Seated)/4s
// Totals list will track an avatars TOTAL DAMAGE over the lifetime of the vehicle.
// For the sake of the antigrief functioning, PROC has to be cleared before it can die. But other than that, damage is now processed when you recieve it and not with a 1s proc delay.
// Also has lazy namespace dropping, if it's just a key or a float/integer it gets dropped because that's baby grief, if antigrief = 1 it blacklists
// if((key)n)return;
// if ((string)((float)n)==n||(string)((integer)n)==n)return;

---
## [IAMLegEndIAM/THEARENUKRISTOLENICSUBUDOPENDR](https://github.com/IAMLegEndIAM/THEARENUKRISTOLENICSUBUDOPENDR)@[c26cb353ce...](https://github.com/IAMLegEndIAM/THEARENUKRISTOLENICSUBUDOPENDR/commit/c26cb353ce1d222b6fcfb5be105bfa6eec50039d)
#### Thursday 2022-05-05 05:26:16 by IAMLegEndIAM

GANG STALKING AND HARASSMENT (#2)

I HAVE BEEN SUFFERING FROM THE EFFECTS OF PTSD AND STOCKHOLMS SYNDROME AS A RESULT OF BEING THE VICTIM OF GANGSTALKING VIA THE 

MK ULTRA PROJECT 

AND 

DIRECT ENERGY WEAPONIZATION VIA USES OF RADIO WAVES SOUND FREQUENCY AND COSMIC MICROWAVE  BACKGROUND ENERGY


I AM CURRENTLY BEING USED AS AN EXPERIMENT BY MY BOYFRIENDS FAMILY AS THEY ARE RELATIVELY DIFFERENT FROM OTHER PEOPLE SO TO SPEAK. 


I REALLY WOULD LIKE TO BE ABLE TO GET OUT OF THIS SITUATION BUT I AM LITERALLY BEING KEPT IN HIS HOUSE AS IT IS A SAFE HOUSE (HUMAN AND SEX TRAFFICKING) I AM A VICTIM OF MODERN SLAVERY AND BECAUSE MY MOTHER HAS RUINED MY REPUTATION BY SLANDERING ME AND DEFAMING MY CHARACTER WITH A WHOLE HELL OF A LOT OF LIES I AN INCAPABLE OF DOING MANY THINGS AT THE MOMENT UNLESS I AM ABLE TO FIND FUNDING TO OBTAIN A LAWYER AND SUE HER AND GET MY CONSERVATORY RIGHTS BACK. IT IS ESSENTIALLY ANOTHER BRITNEY SPEARS CASE ONLY MUCH WORSE. 


PLEASE ASSIST ME IN ANY WAYS THAT YOU CAN RESOURCES ETC FINDING PROFESSIONALS TO CONNECT ME WITH TO SHARE MY STORY AND GET IT OUT THERE SO THAT WAY WE CAN BEGIN THE PROCESS IF TERMINATING HUKAN TRAFFICKING ONCE AND FOR ALL AND I AM THE ONLY ONE THAT CAN DO IT. 


THANKS SO MUCH IN ADVANCE


KRISTEN
NICOLE
DUBUS
PENROD
HUERTA

---
## [anandhan07/kernel_xiaomi_vince](https://github.com/anandhan07/kernel_xiaomi_vince)@[feb1a2209a...](https://github.com/anandhan07/kernel_xiaomi_vince/commit/feb1a2209a9199e2a0319623680395676762ab06)
#### Thursday 2022-05-05 05:49:50 by zenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[f687827809...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/f687827809a2cdbe3ddd4f4d0e41531ae5372078)
#### Thursday 2022-05-05 06:51:23 by umeshl@appynitty.com

Changes done by Millionaire persone and its me I will be Definitley successful in this year and building aesthetics physics for my life in main moto also building new floor from trading profit and create my dream setup in this floor to create youtube videos instagram reels and prove to my self i do it jai shree ram ameen god blessed sai baba blessed me thanku and sorry for any mistake god

---
## [mszeles/a-hamunish-humanish-thoughtishish](https://github.com/mszeles/a-hamunish-humanish-thoughtishish)@[52788ba3ca...](https://github.com/mszeles/a-hamunish-humanish-thoughtishish/commit/52788ba3ca178b5f1b6a0ffeed8cfb0963981a5c)
#### Thursday 2022-05-05 10:03:31 by Miklos Szeles

Neveloper: I think we can publish my thoughts on our blog mszeles.com
Miki: We will get there too, as soon as you will jot 7 of your thoughts, we will publish "Neveloper's Humanish Agileish Thoughts Vol. 1"
Nikolai: Nobody will read this bul.shit.
Neveloper: We will see, Nikolai. We will see.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b3c5a5feab...](https://github.com/mrakgr/The-Spiral-Language/commit/b3c5a5feab4baa91c592f9ed45cbcace985050ad)
#### Thursday 2022-05-05 10:59:13 by Marko Grdinić

"9:50am. Let me chill a bit and I will start. I'll finish the Clice chapter and then move on to texturing. I've watched enough Blender tutorials to last me a lifetime.

10:10am. Let me start. It is time to get this thing out of the way. I can't work on this monitor all my life.

10:10am. I am starting to think that ZenUV is more trouble than its worth.

10:35am. Shit, why aren't fonts in substance painter translucent. What the hell?

https://youtu.be/U4Hwi6fh9ns
Adding Text in Substance Painter

Let me watch this. I could always do the text in CSP and import it, but that'd be such a waste.

https://youtu.be/U4Hwi6fh9ns?t=53

This gives me an idea. Instead of putting them straight into the base layer as color, I could put the text is a mask. That way black won't have an effect. But since I started it, let me watch the video.

https://youtu.be/U4Hwi6fh9ns?t=175

I need to remember that shift is slow drag.

10:50am. Nevermind this, I am just wasting my time watching.

Let me use the mask.

11am. Finally done with the logos. Now I just need some roughness patterns.

11:05am. Filling in the middle of the screen with black was the easiest thing ever thanks to UV chunk. This would have been so much harder if I had loose topology.

Er, let me pause this a bit. I need to go back to the cube. I want to try out a subdiv pattern.

11:10am. No it did not work. There are so many ways of making holes using subdiv it seems.

Now focus me, let me work on texturing the monitor. It is not that hard. I just need to slap some noise.

11:15am. I really hate how substance mask options are organized. Copy and paste mask is in an entirely different place from the rest of the mask menu items.

11:30am. What is the mask background? Nevermind that for now.

11:50am. The screen is textured and done. This was easy. Wish that the fingerprint grunge textures were procedural.

Now comes the rest of them. I'll do the base, the stalk, the skirt, and then I'll be done.

12am. Focus me, stop looking at Rhino deformers. it seems it does have some sculpting functionality.

12:10pm. Ok, I am done. In order for the logo to be clear, I had to use 4k textures, but that is fine.

12:20pm. No wait, I am confused here. I thought that with UDIMs I'd get just two different texture files. But here it is making a separate texture for each material! I am starting to think that I do not understand exports as well as I thought I did.

https://youtu.be/g9uZe-OlzhM
Ultimate guide to substance painter UDIM - UV tile workflow

Let me watch this. If UDIMs are there to separate the materials, then there is no point in packing the UDIMs the way I did.

https://youtu.be/g9uZe-OlzhM?t=54

Using the legacy workflows is always a mistake. I made it too many times.

https://youtu.be/g9uZe-OlzhM?t=133

Yeah, I have them grouped like this.

12:40pm. Hmmmmm...

Fuck.

I fucked up the way I grouped the materials. It makes sense that each shader would be separate. Instead of using separate materials, I should have used geometry masks.

This can't be happening, is there any way I can avoid repeating all the work that I did?

...No this is weird.

It might make sense to output a separate texture for each material on some level, but in that case why is the UV space unified between them?

12:55pm. Let me have breakfast here.

I'll watch some UDIM tutorials after that and redo the work if necessary. As long as I keep the Screen material around, I won't have to redo too much, I'll just have to reassign the rest to it.

I guess I really walked just straight into this one. Texture sets are more confusing than one might think."

---
## [LuisFelipeCoelho/acts](https://github.com/LuisFelipeCoelho/acts)@[6e1fd31474...](https://github.com/LuisFelipeCoelho/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Thursday 2022-05-05 12:08:45 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [ModruKinstealer/CS50ProblemSets](https://github.com/ModruKinstealer/CS50ProblemSets)@[c999730c72...](https://github.com/ModruKinstealer/CS50ProblemSets/commit/c999730c721cf8ed42b6cf4340a2fabd6df7d4bd)
#### Thursday 2022-05-05 13:15:28 by ModruKinstealer

pset 7: Fiftyville

Distribution code provided a blank log.sql file, fiftyville.db, and answers.txt. The rest are files I used to store information from queries I ran for later reference since I get pulled away fairly often and will regularly have hours/days between times to work on the problem.
Problem: CS50 duck was stolen.
What we know: took place on July 28, 2021 and took place on Humphrey Street
What we need: 
    Who the thief is,
    What city the thief escaped to, and
    Who the thief’s accomplice is who helped them escape

Thoughts:
I didn't have much trouble with Syntax on this one. SQL is fairly easy to get along with as far as we've gone. No doubt when you get into real world issues it's way harder but I'm encouraged by this brief exposure to it.
I noted in the log.sql in my final thoughts that I feel like I was really hampered by the way in which I was going about this in that I do these at work where I have the most time easily available. Unfortunately in this case I had hours between times I could work on this, and in a couple cases several days.  I didn't do a good enough job of using the log.sql to refresh my memory of where I was at.  
I also go lost in the weeds a bit in trying to prove who the accomplice was using data from the .db. Typically you'd be able to prove the accomplice bought the tickets for the thief through bank transactions and we couldn't do that here. This scenario was more simplistic in this regards and ultimately you just need to know who the thief called that day.
Lastly, I was trying to not use hardcoded information in my queries based on a general thought that hardcoding things in programs is bad and you should store it in a variable so you can maintain it easier in the future. In this particular scenario that hindered more than helped and caused me to spend a significant amount of time trying to work with sub-queries I didn't really need to when I could just go more linearly and reduce results with prior query info.

---
## [BuzzyBox/GameDebugMode](https://github.com/BuzzyBox/GameDebugMode)@[38ef28131e...](https://github.com/BuzzyBox/GameDebugMode/commit/38ef28131e0e0f3c6056dc144a92152fff370c98)
#### Thursday 2022-05-05 14:50:03 by BuzzyBox

Debug 12

Actually done a lot today even though it isn't much it my achievement haha!
I decided to make the choices into the text dialogue code and I had such trouble figuring out how to make the shopping menu pop up!
But in the end I did remember to make another function to go within the clickable choices menu which was really annoying but I am super glad that I managed to figure out in the end!

---
## [SmArtKar/tgstation](https://github.com/SmArtKar/tgstation)@[ce0aff7526...](https://github.com/SmArtKar/tgstation/commit/ce0aff7526158133acd1b53bd5d2d9d6ac9578f3)
#### Thursday 2022-05-05 15:47:16 by GoldenAlpharex

Fixed Icebox's lower two z-levels not being included in the Map Compile action (#66503)

Did you know that you could currently put a bunch of random shit in the lower levels of icebox and the map compile would be none the wiser?

I sure did.

I hate that it's done manually this way, but honestly it's not worth refactoring the whole action to make it work differently.

Ensuring that the lower levels work properly is, in fact, a good thing.

---
## [google/wireit](https://github.com/google/wireit)@[c85c022769...](https://github.com/google/wireit/commit/c85c02276975a1a86cbf509a7e9a353d5f0a19a8)
#### Thursday 2022-05-05 16:33:45 by Alexander Marks

Error when trying to cache outside of package (#182)

It's currently not possible to locally cache an output file that isn't inside of the package directory. We check for this case when we delete and throw, but not when we cache. So if you are caching but have cleaning disabled, we would silently weirdly save the output file to a parent directory, and then not restore it.

Now this is an error.

Note we could in theory do this during analysis, but I'm not 100% confident in my ability to correctly detect this case given all of the possible magic glob syntax, so for now it's safer to just do it at runtime. (see https://github.com/google/wireit/issues/64).

Also note we could in theory support caching files outside of the package root, but we'd have to do something like a tarball for the local cache, instead of simply copying into `.wireit/<script>/cache/<hash>`. We should think carefully about whether we want to do that, though, so I'm not dealing with that for now.

Fixes https://github.com/google/wireit/issues/181

---
## [Goratrix/goratrix-crawl](https://github.com/Goratrix/goratrix-crawl)@[c08b2e8bf8...](https://github.com/Goratrix/goratrix-crawl/commit/c08b2e8bf8864494d43077b7622612e4c5b192df)
#### Thursday 2022-05-05 17:02:16 by nicolae-carpathia

Add the most nicolae demonic rune vault possible (#2260)

* Add the most nicolae demonic rune vault possible

I have reached my apotheosis: I have put a rune in a shop.

Since the demonic rune repeats if you don't pick it up, I figured it
would be the best option for a rune shop. (The abyssal rune also
reappears if you don't pick it up, but the theme is easier to fit into
Pandemonium.) If you already have the rune, the shop instead places
another kind of rarity: a figurine of a ziggurat. (The only other
really rare item I could think of was a quad damage, and I've been
explicitly told multiple times that I'm not allowed to use those
outside of Sprint. Tyranny!)

Out of 25 generated shops, the stats on the price of a demonic rune:
Minimum: 3804
Maximum: 8647
Average: 6640.76
St Dev:  1412.1
I didn't check the price stats on the zigfig because the rune is the
real draw here.

The vault also places fat stacks of cash, three other shops, and
demon-summoning monsters from other branches as visitors. Enjoy!

* Make adjustments to the pan bazaar rune vault

Make some changes based on feedback from the other devs:
1) If you already have the demonic rune, instead of selling a
   zigfig, the central shop now just sells randarts. (I had
   underestimated the importance of zigfigs.)
2) The difficulty has been turned up a bit. The area outside
   the central area places more monsters now.
3) A few of the nonruniferous shops have been tweaked.

---
## [RoundtableHold/roundtablehold.github.io](https://github.com/RoundtableHold/roundtablehold.github.io)@[07161f103d...](https://github.com/RoundtableHold/roundtablehold.github.io/commit/07161f103d851b6b863d25c50950515adf1a007b)
#### Thursday 2022-05-05 17:44:47 by Olivia

Landmarks Overhaul pt 1

- The Evergaols and Legacy Dungeons pages are completely gone. I removed the yaml and html files. Their progress will be lost.
- The Caves page has been completely redone to become a Landmarks page. The page has been renamed to Landmarks & Locations and the yaml is renamed to landmarks.yaml. The id is still caves so that progress from Caves, Catacombs, and Tunnels is preserved on this new page.
- Content from the two deleted pages has been moved to the Landmarks page. Their ids now follow new conventions to not clash with the existing Caves ids: "e1" - "e10" for evergaols, and "ld1" - "ld14" for legacy dungeons.
- The Location column and description for all preexisting items on the Landmarks page have been removed. It will be made obsolete by map links to every location, though these are not yet implemented.
- Every location in the game that generates a landmark on the in-game map now has an entry on the Landmarks page, dramatically extending the page. For the most part, these new entries don't have notes or other info that'd be good to add yet, but they do all have their correct icons, unless I made any mistakes. Landmarks follow the id convention "l1" - "l130". I think I got all of them, but there's 130 and no list in the game to compare against, so I welcome double and triple checkers.
- The Landmarks page is sorted by location as the Caves page was, with all other integrated items sorted into their places.
- Within region sections, I sorted the locations into consistent orders as best I could, but they will likely need reordering. My order within a region is Caves, Catacombs, Tunnels, Hero's Graves, Evergaols, Minor Erdtrees, Divine Towers, Puzzle Towers, Ruins, Shacks, Churches, Unique, and Legacy Dungeons. I enforced this order with commenting in every section.
- The original Caves page was missing two: Sellia Hideaway and Auriza Side Tomb. These have been added.
- I changed Fort Haight from a legacy dungeon to a simple landmark. Calling it a legacy dungeon seemed a pretty extreme stretch, especially when all other (sometimes bigger) Forts weren't.
- In other tweaks, I renamed rememberances.yaml to be spelled correctly, remembrances.yaml. The page title was spelled correctly, so the html name didn't change and any links should be preserved.
- I moved Incantations below Sorceries in the list of pages, just because it seemed silly that we have Incantations on top when Sorceries are always listed first in-game.
- Next up is linking the locations of all these new Landmarks.

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[3950ba9ff5...](https://github.com/mbs-octoml/mbs-tvm/commit/3950ba9ff5bd4291be37b5c2fe1e41b306873c6d)
#### Thursday 2022-05-05 17:48:53 by Mark Shields

** Collage v2 sketch ***

- cleanup before rebase
- Use 'regular' target when build, not external codegen target
- Tuned for -libs=cudnn
- Tune before collage not during
- Bring over target changes
- Fix GetSpecName
- Try again on python target changes, this time leave check_and_update_host_consist unchanged
- Revert python target changes to try again less agressively
- Few other cleanups
- Switch to 'external codegen targets' style
- Woops, run just_tvm after collage to pick up tuning logs
- Finish tuning for rtx3070
- Run them all!
- Update tuning logs
- Share global vars in the candidate function cache
- Finished tuning mobilenet, started on resnet50.
- Include model name in logs to make sure we don't get anything mixed up
- Drop -arch=sm_80
- Fix MaxCoalesce
- Attach external_symbol to lifted functions
- Add missing node registration, but leave VisitAttrs empty for now
- Make MaxCoalesce as aggressive as possible, since simple impl did not handle sharing.
- Finish tuning resnext50
- Improve coelescing
- Account for coelesced functions when outlining final module
- Fix caching, for real this time.
- More nn.conv2d autotvm tuning records, but still not done with resnext50_32_4d.
- OutlineExternalFunction both when preparing to estimate cost and after optimal
  partitioning applied.
- Use fp16 in TensorRT only if model's 'main_dtype' is float16.
- Fix CostEstimator caching issue
- More Target cleanup (while waiting for tuning runs)
- Better logging of candidates
- Support export to ONNX
- Fix merge
- Part-way through tuning for mobilenet.
- Add resnext50_32x4d
- Lift all "Compiler" functions before estimating to ensure no Relay passes are run on them
- Still trying
- Trying to track down weird failure in conv2d compute.
- Switch tensorrt to be fully pattern & composite function based
- Combiner rule for tuple projection
- Allow build to fail in estimate_seconds
- Add mobilenetv2 and resnet50v2 to menagerie
- Update CompilationConfig to handle target refinement
- Nuke remaining uses of TargetMap in favor of CompilationConfig
  (still needs to be pushed into python side)
- Save/Load dso libraries (needed for Cutlass with separated run)
- Move models into separate file
- gpt2_extract_16 and autotvm tuning log
- Handle missing tuning log files
- fp16 support in scalars and the tensorrt runtime.
- Wrap runner in nsys nvprof if requested
- Enforce strict compile/run time separation in preparation for profiling
- Better logging of final optimal partitioning and state of all candidates
- Fix handling of tuples and InlineComposites fixup pass.
- Fix TensorRT pattern bugs
- Pass max_max_depth via PassContext
- Better logging so can quickly compare specs
- BUG: Benchmark the partitioned rather than original model!!!
- Use median instead of mean
- Back to GPT2
- Make sure all function vars have a type
- Don't extract tasks if estimating BYOC-only
  (Was double-tuning every cutlass kernel).
- Make sure cudnn pattern table is registered
- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---
## [NOUIY/aws-cdk](https://github.com/NOUIY/aws-cdk)@[c071367def...](https://github.com/NOUIY/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Thursday 2022-05-05 19:51:50 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [mayhemheroes/gitea](https://github.com/mayhemheroes/gitea)@[3725fa28cc...](https://github.com/mayhemheroes/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Thursday 2022-05-05 20:44:04 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [ExpHP/truth](https://github.com/ExpHP/truth)@[93b985269d...](https://github.com/ExpHP/truth/commit/93b985269dd714f7a7cabd73ac7fe91a22d9c898)
#### Thursday 2022-05-05 21:55:59 by Michael Lamparski

add --output option to decompilation

Somebody is having trouble with decompilation producing mojibake
in the output file.  I think > for output redirection might not work
so well on CMD. (maybe '>' does ANSI? maybe rust is writing UTF-8 to
the ANSI APIs? I don't know. First let's find out if this even works!)

An --output option should resolve this problem by making text encodings
a non-issue (the OS must assume we're writing binary).  And honestly,
not having it just feels assymetric compared to compilation, so it
should be there anyways.

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[a583c6964c...](https://github.com/sunamo/sunamo/commit/a583c6964c494904ba9cf2f395a270441ff0c478)
#### Thursday 2022-05-05 22:08:58 by Radek Jancik

Well, yeah. At a certain point, you've got to be really honest with yourself. Like, 'Why am I doing this? What are my motivations?' Like, if you get into it because you want to be famous? Then you've got a long row to hoe. But if you really feel like it's a labour of love and it's something you're actually legitimately good at, then it's not that hard to keep plugging away. - Will Arnett

---

