import unittest
import re


class Tests(unittest.TestCase):

    def test_strip(self):
        count = dict()
        for line in MESSAGE_01.splitlines():
            tag = line[:6]
            if tag:
                count[tag] = count.get(tag, 0) + 1

        print(count)

    def test_re(self):
        r = re.compile(" a+h+ ")
        self.assertEqual(
            [" ah "],
            r.findall(" ah "),
        )
        self.assertEqual(
            [" aaahhhh "],
            r.findall(" aaahhhh "),
        )


MESSAGE_01 = "Update 0.4.0 release (#10)\n\n* Added per section InfoLevel and DC Diagnostic HealthCheck\r\n\r\n* Added a function to convert bytes automatically to GB or TB based on size\r\n\r\n* Added a function to convert true or false automatically to Yes or No. Hate Switch cases\r\n\r\n* Added initial report structure\r\n\r\n* Convert true or false output to yes or no\r\n\r\n* Add Active Directory version support, Module Requirements and examples\r\n\r\n* Fix forwrong false case\r\n\r\n* Fix string output\r\n\r\n* Update function name\r\n\r\n* Add function with new name\r\n\r\n* Update the functions to filter the content by Domain\r\n\r\n* Update switch case\r\n\r\n* Add Organization Unit reporting\r\n\r\n* Pscribo Message fix\r\n\r\n* Add site replication health check\r\n\r\n* Fix created time format\r\n\r\n* Add site links to the site report function\r\n\r\n* Add site replication function\r\n\r\n* Update funtion to better handle DC unavailable situations\r\n\r\n* Add Site replication to the main report also fix InfoLevel\r\n\r\n* Section Style Rename\r\n\r\n* Add code to better handle unavailable DC Server\r\n\r\n* Add Domain Controller Time Source Function also fix misc issues\r\n\r\n* Added funtion to check AD Services status (DNS,NTP, NTDS etc)\r\n\r\n* Add code to beter catch AD Domain issues\r\n\r\n* Add support to Microsoft Active Directory Group Policy Objects information\r\n\r\n* Update section heading text\r\n\r\n* Add support to Microsoft AD Domain Name System Infrastructure information\r\n\r\n* Add GPO support in Domain Section also added new DNS Section\r\n\r\n* Add more healthcheck support\r\n\r\n* update version to 0.2.0\r\n\r\n* Add support for DNS Zone information\r\n\r\n* Ensure support for PSv5.1+\r\n\r\n* Update changelog with initial release features\r\n\r\n* Updated Readme Module Requirements and installation examples\r\n\r\n* Updated required permissions\r\n\r\n* Update functions to use pssession\r\n\r\n* Added more try\\catch conditions also improve verbose/debug logging\r\n\r\n* implement a shared function util file\r\n\r\n* Added misc documentation\r\n\r\n* Updated changelog for 0.2.0 changes\r\n\r\n* Fix FQDN text\r\n\r\n* Add more Examples\r\n\r\n* Fix misc text\r\n\r\n* More fixes\r\n\r\n* Added Known Issues\r\n\r\n* Added sample report\r\n\r\n* The never ending fixes (Readme)\r\n\r\n* Readme Fixes :(\r\n\r\n* Readme example fixes\r\n\r\n* requested recomendation\r\n\r\n* Added DHCP Server Section\r\n\r\n* Fix for PSSession exhaustion\r\n\r\n* Minot text fix & Error message catching\r\n\r\n* Fix duplicate pssession error\r\n\r\n* Fix for unhandle null values\r\n\r\n* Fix for PSSession exhaustion also added DHCP main section\r\n\r\n* Added more dhcp sections\r\n\r\n* Added Heading6 to the document style\r\n\r\n* Fix for heading hierarchy\r\n\r\n* Fix schema version code\r\n\r\n* Added funtion to convert from subnetmask to dotted notation\r\n\r\n* Added definition paragraph also fix heading hierarchy\r\n\r\n* Added Heading 7 definition\r\n\r\n* Updated ActiveDirectory RequiredModules fix bug on issues #3\r\n\r\n* Updated section Title\r\n\r\n* Added IPv4/IPv6 Scope section\r\n\r\n* Added better error message\r\n\r\n* Fix IPaddress colums\r\n\r\n* Update version to 0.3.0\r\n\r\n* Fix lease duration unlimited case\r\n\r\n* Update to release version 0.3.0\r\n\r\n* Added reference to WinRM requirements\r\n\r\n* Added security section to ReportConfig json\r\n\r\n* Added Scope Option information\r\n\r\n* Added Scope Option section and impleme more InfoLevel structure\r\n\r\n* Remove the Import PSPKI also added InfoLevel information\r\n\r\n* Rename perScopeOptions ti perScopeSetting\r\n\r\n* Rename ScopeSetting function on main report script\r\n\r\n* Remove unused Site InfoLevel\r\n\r\n* Fix minor text error\r\n\r\n* Added dcdiag healthcheck\r\n\r\n* Added GPO healthcheck also update comments\r\n\r\n* Implement Domain InfoLevel 2\r\n\r\n* Fix for diagnosting messages\r\n\r\n* Added GPO Owner HealthCheck\r\n\r\n* Added Tombstone Lifetime to Forest Section\r\n\r\n* Implement InfoLeve 2 and added more DC Inventory Info\r\n\r\n* Implement DNS Infolevel 2\r\n\r\n* Added Installed Roles and Features to the DC section\r\n\r\n* Added  more IPv6 Dhcp content\r\n\r\n* Added more DNS InfoLevel 2\r\n\r\n* Added more DHCP IPv6 content\r\n\r\n* Change InfoLevel settings\r\n\r\n* Added more DHCP IPv6 content\r\n\r\n* Added DHCP BestPractice HealthCheck\r\n\r\n* Added DHCP HealthCheck\r\n\r\n* More DHCP HealthChecks\r\n\r\n* Added DHCP IPv6 per scope settings\r\n\r\n* Added DNS Conditional Forwarder to DNS Section partialy fix issue #6\r\n\r\n* Split Domain Section files\r\n\r\n* Added DC definition also added  DHCP IPv6 per scope setting to main script\r\n\r\n* Translate DN to Name\r\n\r\n* Added Fined Grained Password Policies to report partially fix issue #6\r\n\r\n* added function to translate Active Directory DN to a meaningfull object\r\n\r\n* Added sessiont to the function Get-AbrADDomainObject\r\n\r\n* Added Log and SysVol Path to NTDS Table to partially fix issue #6\r\n\r\n* Fix for remove pssession\r\n\r\n* Fix for DC FQDN\r\n\r\n* Fix to DN object\r\n\r\n* Fix Heading index\r\n\r\n* Added more object count to implement #9 improvements\r\n\r\n* GPO health checks has been added to comply with improvements in #9.\r\n\r\n* initial CA section commit\r\n\r\n* Fix heading grammar\r\n\r\n* Fix Section heading grammar\r\n\r\n* Minor fix to True/False translation\r\n\r\n* Added domain variable to get-gpo cmdlet\r\n\r\n* Added Health Check - Enforced Group Policy Objects Summary. Partially fix #\r\n\r\n* Added Health Check - Enforced Group Policy Objects Summary. Partially fix #9\r\n\r\n* Added Health Check  for GPO Blocked Inheritance. Another Fix for #9\r\n\r\n* Fixed Verbose logging\r\n\r\n* Added function to convert DN to Canonical\r\n\r\n* Misc grammar fix\r\n\r\n* Disable Certificate Authority for now\r\n\r\n* More code verification\r\n\r\n* Fix  Section HEading\r\n\r\n* Make sure pssession are properly closed\r\n\r\n* Added GPO Logon/Logoff Startup/Shutdown Script support. Fix for issue #9\r\n\r\n* Added detailed InfoLevel also remove CA and Security Section\r\n\r\n* Update version to 0.4.0\r\n\r\n* Fix for unexpected count on PowerShell v5+\r\n\r\n* Update Sample Report\r\n\r\n* Update Changelog with 0.4.0 changes\r\n\r\nCo-authored-by: Tim Carman <tpcarman@gmail.com>"
