import unittest
from pathlib import Path

from .good_messages import GoodMessages

PROJECT_PATH = Path(__file__).resolve().parent.parent
STASH_PATH = PROJECT_PATH / "stash"


REPEATING_LINES = [
    "Update 0.4.0 release (#10)\n\n* Added per section InfoLevel and DC Diagnostic HealthCheck\r\n\r\n* Added a function to convert bytes automatically to GB or TB based on size\r\n\r\n* Added a function to convert true or false automatically to Yes or No. Hate Switch cases\r\n\r\n* Added initial report structure\r\n\r\n* Convert true or false output to yes or no\r\n\r\n* Add Active Directory version support, Module Requirements and examples\r\n\r\n* Fix forwrong false case\r\n\r\n* Fix string output\r\n\r\n* Update function name\r\n\r\n* Add function with new name\r\n\r\n* Update the functions to filter the content by Domain\r\n\r\n* Update switch case\r\n\r\n* Add Organization Unit reporting\r\n\r\n* Pscribo Message fix\r\n\r\n* Add site replication health check\r\n\r\n* Fix created time format\r\n\r\n* Add site links to the site report function\r\n\r\n* Add site replication function\r\n\r\n* Update funtion to better handle DC unavailable situations\r\n\r\n* Add Site replication to the main report also fix InfoLevel\r\n\r\n* Section Style Rename\r\n\r\n* Add code to better handle unavailable DC Server\r\n\r\n* Add Domain Controller Time Source Function also fix misc issues\r\n\r\n* Added funtion to check AD Services status (DNS,NTP, NTDS etc)\r\n\r\n* Add code to beter catch AD Domain issues\r\n\r\n* Add support to Microsoft Active Directory Group Policy Objects information\r\n\r\n* Update section heading text\r\n\r\n* Add support to Microsoft AD Domain Name System Infrastructure information\r\n\r\n* Add GPO support in Domain Section also added new DNS Section\r\n\r\n* Add more healthcheck support\r\n\r\n* update version to 0.2.0\r\n\r\n* Add support for DNS Zone information\r\n\r\n* Ensure support for PSv5.1+\r\n\r\n* Update changelog with initial release features\r\n\r\n* Updated Readme Module Requirements and installation examples\r\n\r\n* Updated required permissions\r\n\r\n* Update functions to use pssession\r\n\r\n* Added more try\\catch conditions also improve verbose/debug logging\r\n\r\n* implement a shared function util file\r\n\r\n* Added misc documentation\r\n\r\n* Updated changelog for 0.2.0 changes\r\n\r\n* Fix FQDN text\r\n\r\n* Add more Examples\r\n\r\n* Fix misc text\r\n\r\n* More fixes\r\n\r\n* Added Known Issues\r\n\r\n* Added sample report\r\n\r\n* The never ending fixes (Readme)\r\n\r\n* Readme Fixes :(\r\n\r\n* Readme example fixes\r\n\r\n* requested recomendation\r\n\r\n* Added DHCP Server Section\r\n\r\n* Fix for PSSession exhaustion\r\n\r\n* Minot text fix & Error message catching\r\n\r\n* Fix duplicate pssession error\r\n\r\n* Fix for unhandle null values\r\n\r\n* Fix for PSSession exhaustion also added DHCP main section\r\n\r\n* Added more dhcp sections\r\n\r\n* Added Heading6 to the document style\r\n\r\n* Fix for heading hierarchy\r\n\r\n* Fix schema version code\r\n\r\n* Added funtion to convert from subnetmask to dotted notation\r\n\r\n* Added definition paragraph also fix heading hierarchy\r\n\r\n* Added Heading 7 definition\r\n\r\n* Updated ActiveDirectory RequiredModules fix bug on issues #3\r\n\r\n* Updated section Title\r\n\r\n* Added IPv4/IPv6 Scope section\r\n\r\n* Added better error message\r\n\r\n* Fix IPaddress colums\r\n\r\n* Update version to 0.3.0\r\n\r\n* Fix lease duration unlimited case\r\n\r\n* Update to release version 0.3.0\r\n\r\n* Added reference to WinRM requirements\r\n\r\n* Added security section to ReportConfig json\r\n\r\n* Added Scope Option information\r\n\r\n* Added Scope Option section and impleme more InfoLevel structure\r\n\r\n* Remove the Import PSPKI also added InfoLevel information\r\n\r\n* Rename perScopeOptions ti perScopeSetting\r\n\r\n* Rename ScopeSetting function on main report script\r\n\r\n* Remove unused Site InfoLevel\r\n\r\n* Fix minor text error\r\n\r\n* Added dcdiag healthcheck\r\n\r\n* Added GPO healthcheck also update comments\r\n\r\n* Implement Domain InfoLevel 2\r\n\r\n* Fix for diagnosting messages\r\n\r\n* Added GPO Owner HealthCheck\r\n\r\n* Added Tombstone Lifetime to Forest Section\r\n\r\n* Implement InfoLeve 2 and added more DC Inventory Info\r\n\r\n* Implement DNS Infolevel 2\r\n\r\n* Added Installed Roles and Features to the DC section\r\n\r\n* Added  more IPv6 Dhcp content\r\n\r\n* Added more DNS InfoLevel 2\r\n\r\n* Added more DHCP IPv6 content\r\n\r\n* Change InfoLevel settings\r\n\r\n* Added more DHCP IPv6 content\r\n\r\n* Added DHCP BestPractice HealthCheck\r\n\r\n* Added DHCP HealthCheck\r\n\r\n* More DHCP HealthChecks\r\n\r\n* Added DHCP IPv6 per scope settings\r\n\r\n* Added DNS Conditional Forwarder to DNS Section partialy fix issue #6\r\n\r\n* Split Domain Section files\r\n\r\n* Added DC definition also added  DHCP IPv6 per scope setting to main script\r\n\r\n* Translate DN to Name\r\n\r\n* Added Fined Grained Password Policies to report partially fix issue #6\r\n\r\n* added function to translate Active Directory DN to a meaningfull object\r\n\r\n* Added sessiont to the function Get-AbrADDomainObject\r\n\r\n* Added Log and SysVol Path to NTDS Table to partially fix issue #6\r\n\r\n* Fix for remove pssession\r\n\r\n* Fix for DC FQDN\r\n\r\n* Fix to DN object\r\n\r\n* Fix Heading index\r\n\r\n* Added more object count to implement #9 improvements\r\n\r\n* GPO health checks has been added to comply with improvements in #9.\r\n\r\n* initial CA section commit\r\n\r\n* Fix heading grammar\r\n\r\n* Fix Section heading grammar\r\n\r\n* Minor fix to True/False translation\r\n\r\n* Added domain variable to get-gpo cmdlet\r\n\r\n* Added Health Check - Enforced Group Policy Objects Summary. Partially fix #\r\n\r\n* Added Health Check - Enforced Group Policy Objects Summary. Partially fix #9\r\n\r\n* Added Health Check  for GPO Blocked Inheritance. Another Fix for #9\r\n\r\n* Fixed Verbose logging\r\n\r\n* Added function to convert DN to Canonical\r\n\r\n* Misc grammar fix\r\n\r\n* Disable Certificate Authority for now\r\n\r\n* More code verification\r\n\r\n* Fix  Section HEading\r\n\r\n* Make sure pssession are properly closed\r\n\r\n* Added GPO Logon/Logoff Startup/Shutdown Script support. Fix for issue #9\r\n\r\n* Added detailed InfoLevel also remove CA and Security Section\r\n\r\n* Update version to 0.4.0\r\n\r\n* Fix for unexpected count on PowerShell v5+\r\n\r\n* Update Sample Report\r\n\r\n* Update Changelog with 0.4.0 changes\r\n\r\nCo-authored-by: Tim Carman <tpcarman@gmail.com>"
    , "linux-yocto/5.4: update to v5.4.82\n\nUpdating linux-yocto/5.4 to the latest korg -stable release that comprises\nthe following commits:\n\n    ec274ecd62f9 Linux 5.4.82\n    4460a7c979ee RDMA/i40iw: Address an mmap handler exploit in i40iw\n    07434172c58b tracing: Remove WARN_ON in start_thread()\n    6ad995b851cb Input: i8042 - add ByteSpeed touchpad to noloop table\n    dfe5d9a8307e Input: xpad - support Ardwiino Controllers\n    c38a7023c00a ALSA: usb-audio: US16x08: fix value count for level meters\n    8cd76dacd3dc net/mlx5: Fix wrong address reclaim when command interface is down\n    2598dd80b801 net/mlx5: DR, Proper handling of unsupported Connect-X6DX SW steering\n    8f92330b0873 net/sched: act_mpls: ensure LSE is pullable before reading it\n    1086f789060a net: openvswitch: ensure LSE is pullable before reading it\n    ba203b92a829 net: skbuff: ensure LSE is pullable before decrementing the MPLS ttl\n    892e08e0b4f3 net: mvpp2: Fix error return code in mvpp2_open()\n    7c3894f695e4 chelsio/chtls: fix a double free in chtls_setkey()\n    178da08f9b5b vxlan: fix error return code in __vxlan_dev_create()\n    5405a299b8c1 net: pasemi: fix error return code in pasemi_mac_open()\n    dc469f423654 cxgb3: fix error return code in t3_sge_alloc_qset()\n    8bfe5b73b185 net/x25: prevent a couple of overflows\n    187a6daf5db4 net: ip6_gre: set dev->hard_header_len when using header_ops\n    a6cd76132872 geneve: pull IP header before ECN decapsulation\n    2b714b607f24 inet_ecn: Fix endianness of checksum update when setting ECT(1)\n    9a3cce1ceee4 ibmvnic: Fix TX completion error handling\n    40caea31dd56 ibmvnic: Ensure that SCRQ entry reads are correctly ordered\n    d126c30eb30d chelsio/chtls: fix panic during unload reload chtls\n    8a1bb298f75f dt-bindings: net: correct interrupt flags in examples\n    af0b082e16fb ipv4: Fix tos mask in inet_rtm_getroute()\n    4615228a50f9 netfilter: bridge: reset skb->pkt_type after NF_INET_POST_ROUTING traversal\n    294de8933adb sched/fair: Fix unthrottle_cfs_rq() for leaf_cfs_rq list\n    c4405cdf96f4 ima: extend boot_aggregate with kernel measurements\n    733729d3e0e4 staging/octeon: fix up merge error\n    6dd37fdc9550 bonding: wait for sysfs kobject destruction before freeing struct slave\n    beead010654d usbnet: ipheth: fix connectivity with iOS 14\n    f057c4d226f1 tun: honor IOCB_NOWAIT flag\n    538008749df2 tcp: Set INET_ECN_xmit configuration in tcp_reinit_congestion_control\n    9a62c8229cff sock: set sk_err to ee_errno on dequeue from errq\n    7f0ddd41e289 rose: Fix Null pointer dereference in rose_send_frame()\n    f2f25bc79782 net/tls: Protect from calling tls_dev_del for TLS RX twice\n    a6300aedf862 net/tls: missing received data after fast remote close\n    a15beea80e72 net/af_iucv: set correct sk_protocol for child sockets\n    9414855a1305 ipv6: addrlabel: fix possible memory leak in ip6addrlbl_net_init\n    99b5382bffd5 devlink: Hold rtnl lock while reading netdev attributes\n    42af416d7146 Linux 5.4.81\n    cd7343987376 ASoC: Intel: Skylake: Automatic DMIC format configuration according to information from NHLT\n    6ebb6af62721 ASoC: Intel: Multiple I/O PCM format support for pipe\n    b2b05b04d44d ASoC: Intel: Skylake: Await purge request ack on CNL\n    a28144d62ddc ASoC: Intel: Allow for ROM init retry on CNL platforms\n    4029a29f93ef ASoC: Intel: Skylake: Shield against no-NHLT configurations\n    754df2d3349d ASoC: Intel: Skylake: Enable codec wakeup during chip init\n    6de661f146a2 ASoC: Intel: Skylake: Select hda configuration permissively\n    422c4938f704 ASoC: Intel: Skylake: Remove superfluous chip initialization\n    23b093a2c4f9 USB: core: Fix regression in Hercules audio card\n    cc54f8b8e1cd x86/resctrl: Add necessary kernfs_put() calls to prevent refcount leak\n    d0c4c5a89f5b x86/resctrl: Remove superfluous kernfs_get() calls to prevent refcount leak\n    e799c00a745e x86/speculation: Fix prctl() when spectre_v2_user={seccomp,prctl},ibpb\n    f753e1c02a2e x86/mce: Do not overwrite no_way_out if mce_end() fails\n    62405223bafd irqchip/exiu: Fix the index of fwspec for IRQ type\n    f69d749d5f7f usb: gadget: Fix memleak in gadgetfs_fill_super\n    cad7b76a6129 USB: quirks: Add USB_QUIRK_DISCONNECT_SUSPEND quirk for Lenovo A630Z TIO built-in usb-audio card\n    c775935dfd1e usb: gadget: f_midi: Fix memleak in f_midi_alloc\n    e1a2a3043cc2 USB: core: Change %pK for __user pointers to %px\n    84d04d722b6a spi: bcm2835aux: Restore err assignment in bcm2835aux_spi_probe\n    5849e7dc560b perf probe: Fix to die_entrypc() returns error correctly\n    27193c41d0db perf stat: Use proper cpu for shadow stats\n    dc4d672a3fb5 can: m_can: fix nominal bitiming tseg2 min for version >= 3.1\n    1f076cc1de82 can: m_can: m_can_open(): remove IRQF_TRIGGER_FALLING from request_threaded_irq()'s flags\n    dd8ab85fd88e RDMA/hns: Bugfix for memory window mtpt configuration\n    e69f384e22f1 RDMA/hns: Fix retry_cnt and rnr_cnt when querying QP\n    49b26b969474 platform/x86: toshiba_acpi: Fix the wrong variable assignment\n    fbd3f1d6ef2f platform/x86: thinkpad_acpi: Send tablet mode switch at wakeup time\n    405fd2180583 can: gs_usb: fix endianess problem with candleLight firmware\n    11420c32c1b4 efi: EFI_EARLYCON should depend on EFI\n    0d245cbd939a efivarfs: revert \"fix memory leak in efivarfs_create()\"\n    abae897f283b arm64: tegra: Wrong AON HSP reg property size\n    5c4c6b2be717 optee: add writeback to valid memory type\n    6d371c3e70d7 ibmvnic: fix NULL pointer dereference in ibmvic_reset_crq\n    382383538f68 ibmvnic: fix NULL pointer dereference in reset_sub_crq_queues\n    a447dbb44d44 net: ena: set initial DMA width to avoid intel iommu issue\n    7869696d6c1e nfc: s3fwrn5: use signed integer for parsing GPIO numbers\n    1a831f889db3 i40e: Fix removing driver while bare-metal VFs pass traffic\n    676857f78c1a IB/mthca: fix return value of error branch in mthca_init_cq()\n    22f821fa5cbb powerpc/64s: Fix allnoconfig build since uaccess flush\n    ae6e75b8c6d6 ibmvnic: notify peers when failover and migration happen\n    7b4e9fcf5ec3 ibmvnic: fix call_netdevice_notifiers in do_reset\n    993e42d0f7d6 s390/qeth: fix tear down of async TX buffers\n    ef0f6e36a6d4 s390/qeth: fix af_iucv notification race\n    bb6c548934c9 s390/qeth: make af_iucv TX notification call more robust\n    f29dfa2bf6c7 cxgb4: fix the panic caused by non smac rewrite\n    0410aeb9e04c bnxt_en: Release PCI regions when DMA mask setup fails during probe.\n    db49200b1dad video: hyperv_fb: Fix the cache type when mapping the VRAM\n    d1a7fb15673e bnxt_en: fix error return code in bnxt_init_board()\n    22e10c6bbefc bnxt_en: fix error return code in bnxt_init_one()\n    11b62fd00c62 scsi: ufs: Fix race between shutdown and runtime resume flow\n    559ab6fb7b66 ARM: dts: dra76x: m_can: fix order of clocks\n    1bef5f25a692 arch: pgtable: define MAX_POSSIBLE_PHYSMEM_BITS where needed\n    95b1f326315b batman-adv: set .owner to THIS_MODULE\n    f5672b83fc2d iwlwifi: mvm: write queue_sync_state only for sync\n    f32a1065c930 phy: tegra: xusb: Fix dangling pointer on probe failure\n    acea5424d9d2 ARM: OMAP2+: Manage MPU state properly for omap_enter_idle_coupled()\n    6f87d79ef40d bus: ti-sysc: Fix bogus resetdone warning on enable for cpsw\n    e8060ddddc9f net: dsa: mv88e6xxx: Wait for EEPROM done after HW reset\n    1f5531bb9720 xtensa: uaccess: Add missing __user to strncpy_from_user() prototype\n    3753a62d5760 perf/x86: fix sysfs type mismatches\n    fd81f0711d9c scsi: target: iscsi: Fix cmd abort fabric stop race\n    8814c070e783 scsi: libiscsi: Fix NOP race condition\n    070a9a046d6d dmaengine: pl330: _prep_dma_memcpy: Fix wrong burst size\n    8a2ae7fa5d5c vhost scsi: fix cmd completion race\n    4940816604e3 nvme: free sq/cq dbbuf pointers when dbbuf set fails\n    01968f9af006 proc: don't allow async path resolution of /proc/self components\n    830f4aa73a69 HID: Add Logitech Dinovo Edge battery quirk\n    4d070afa1080 HID: logitech-hidpp: Add HIDPP_CONSUMER_VENDOR_KEYS quirk for the Dinovo Edge\n    204dbc26f14e x86/xen: don't unbind uninitialized lock_kicker_irq\n    d6b5dc5429f1 dmaengine: xilinx_dma: use readl_poll_timeout_atomic variant\n    54b01ded1e92 HID: add HID_QUIRK_INCREMENT_USAGE_ON_DUPLICATE for Gamevice devices\n    cd7ea86a4a64 staging: ralink-gdma: fix kconfig dependency bug for DMA_RALINK\n    b3701c29a468 HID: hid-sensor-hub: Fix issue with devices with no report ID\n    8f68a28c9ecc Input: i8042 - allow insmod to succeed on devices without an i8042 controller\n    dbe67dcf97cf HID: add support for Sega Saturn\n    3845b2117f6d HID: cypress: Support Varmilo Keyboards' media hotkeys\n    604912c2b20e HID: ite: Replace ABS_MISC 120/121 events with touchpad on/off keypresses\n    8a35be6c38aa HID: uclogic: Add ID for Trust Flex Design Tablet\n    733e6db9736d arm64: pgtable: Ensure dirty bit is preserved across pte_wrprotect()\n    b456de294ee4 arm64: pgtable: Fix pte_accessible()\n    8b4d82d8dbff trace: fix potenial dangerous pointer\n    4a301b05cf61 KVM: x86: Fix split-irqchip vs interrupt injection window request\n    b7d2e45cf613 KVM: x86: handle !lapic_in_kernel case in kvm_cpu_*_extint\n    6276d38cce87 KVM: arm64: vgic-v3: Drop the reporting of GICR_TYPER.Last for userspace\n    45b5f4b1b40b KVM: PPC: Book3S HV: XIVE: Fix possible oops when accessing ESB page\n    214e6af4217a cifs: fix a memleak with modefromsid\n    56f639aa0b5d smb3: Handle error case during offload read path\n    afa51221b911 smb3: Avoid Mid pending list corruption\n    1b63215666c0 smb3: Call cifs reconnect from demultiplex thread\n    f923044a6c72 wireless: Use linux/stddef.h instead of stddef.h\n    a6676b0fa09f btrfs: fix lockdep splat when reading qgroup config on mount\n    6ea14731ac4c btrfs: don't access possibly stale fs_info data for printing duplicate device\n    12aedea58281 btrfs: tree-checker: add missing returns after data_ref alignment checks\n    0115a2613397 btrfs: tree-checker: add missing return after error in root_item\n    6ec51459df71 netfilter: clear skb->next in NF_HOOK_LIST()\n    ee791835b3ec ipv4: use IS_ENABLED instead of ifdef\n    9d16996369fd spi: bcm2835: Fix use-after-free on unbind\n    b606031bbfed spi: bcm-qspi: Fix use-after-free on unbind\n\nSigned-off-by: Bruce Ashfield <bruce.ashfield@gmail.com>\nSigned-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>\n(cherry picked from commit ad12cda067ffee809d133a1d21599c9f3ef06435)\nSigned-off-by: Steve Sakoman <steve@sakoman.com>"
]


class Tests(unittest.TestCase):

    def test_repetitive_lines(self):
        proc = GoodMessages(verbose=True)
        for rep_lines in REPEATING_LINES:
            self.assertTrue(
                proc.has_too_much_repetitive_line_starts(rep_lines)
            )

    def test_remove_duplicates(self):
        proc = GoodMessages(verbose=True)
        proc.commits = [
            {"commit": {"message": "abcdefghijklmnopq"}},
            {"commit": {"message": "123456789"}},
            {"commit": {"message": "abcdefghijklmnopq"}},
            {"commit": {"message": "blabla"}},
            {"commit": {"message": "abcde123456789abcde"}},  # middle third still matches
            {"commit": {"message": "blub"}},
        ]
        proc.remove_duplicates()
        self.assertEqual(
            [
                {"commit": {"message": "abcdefghijklmnopq"}},
                {"commit": {"message": "123456789"}},
                {"commit": {"message": "blabla"}},
                {"commit": {"message": "blub"}},
            ],
            proc.commits
        )

    # TODO: would be great to de-duplicate the messages
    #   but it's complicated... They are all a bit different.
    @unittest.expectedFailure
    def test_remove_duplicate_with_slight_changes(self):
        M1 = "Include full register state in ARM Cortex M Exception Stack Frame (ESF)\n\n**Is your enhancement proposal related to a problem? Please describe.**\n\nTo debug hard-to-reproduce faults/panics, it's helpful to get the full\nregister state at the time the fault occurred. This enables recovering\nfull backtraces and the state of local variables at the time a fault\ntook place. Pretty much all OSs and even some RTOS (i.e mynewt,\nesp-idf) support this in some fashion (i.e coredumps, mini-dumps,\nlinux kernel oops, etc) and it would be awesome if Zephyr could too!\n\nToday this is not possible with the ARM Cortex M Zephyr port for two main reasons:\n\n1). A [copy](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L961-L962)\nof the original hardware exception stack frame is made before calling\nk_sys_fatal_error_handler(). This means the stack pointer prior to the\nexception cannot be recovered making it impossible to recover the full\nbacktrace.\n\n2). Registers that are callee-saved (r4-r11 & exc_return) are not\ncollected in z_arm_fault() which means when k_sys_fatal_error_handler\nis called the register state is not readily available. This\ninformation is needed to accurately recover local variable state\nleading up to a crash.\n\n\n**Describe the solution you'd like**\n\nTo fix these issues and enable better diagnostic facilities, I'd like\nto update the [`z_arch_esf_t` implementation for ARM aarch32](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/include/arch/arm/aarch32/exc.h#L76-L92)\nto pass the original hardware exception frame pointer as well as\ncallee-saved registers.\n\n\n```c\nstruct __full_esf {\n\tstruct __esf *exception_frame;\n\tstruct __callee_saved_esf *callee_regs;\n};\n\ntypedef struct __full_esf z_arch_esf_t;\n```\n\n**Describe alternatives you've considered**\n\nI think there are several different ways the full stack frame could be\nexposed from [z_arm_fault()](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L934-L978). I\ntried to use an approach that would allow the information to be\nexposed via the k_sys_fatal_error_handler API.\n\n**Additional context**\n\nI've been using patches to achieve this behavior on the last few\nZephyr releases but I'd love to upstream the work so it's more\naccessible to others. I've put together a working implementation\n[here]() against the current master branch. Happy to open a PR for\nreview if the idea makes sense to folks!"
        M2 = "Include full register state in ARM Cortex M Exception Stack Frame (ESF)\n\n**Is your enhancement proposal related to a problem? Please describe.**\n\nTo debug hard-to-reproduce faults/panics, it's helpful to get the full\nregister state at the time the fault occurred. This enables recovering\nfull backtraces and the state of local variables at the time a fault\ntook place.\n\nPretty much all OSs and even some RTOS (i.e mynewt,\nesp-idf) support this in some fashion (i.e coredumps, mini-dumps,\nlinux kernel oops, etc) and it would be awesome if Zephyr could too!\n\nToday this is not possible with the ARM Cortex M Zephyr port for two main reasons:\n\n1). A [copy of the original hardware exception stack frame](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L961-L962)\nis made before calling k_sys_fatal_error_handler(). This means the\nstack pointer prior to the exception cannot be recovered making it\nimpossible to recover the full backtrace.\n\n2). Registers that are callee-saved (r4-r11 & exc_return) are not\ncollected in z_arm_fault() which means when k_sys_fatal_error_handler\nis called the register state is not readily available. This\ninformation is needed to accurately recover local variable state\nleading up to a crash.\n\n\n**Describe the solution you'd like**\n\nTo fix these issues and enable better diagnostic facilities, I'd like\nto update the [`z_arch_esf_t` implementation for ARM aarch32](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/include/arch/arm/aarch32/exc.h#L76-L92)\nto pass the original hardware exception frame pointer as well as\ncallee-saved registers.\n\n\n```c\nstruct __full_esf {\n\tstruct __esf *exception_frame;\n\tstruct __callee_saved_esf *callee_regs;\n};\n\ntypedef struct __full_esf z_arch_esf_t;\n```\n\n**Describe alternatives you've considered**\n\nI think there are several different ways the full stack frame could be\nexposed from [z_arm_fault()](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L934-L978). I\ntried to use an approach that would allow the information to be\nexposed via the k_sys_fatal_error_handler API.\n\n**Additional context**\n\nI've been using patches to achieve this behavior on the last few\nZephyr releases but I'd love to upstream the work so it's more\naccessible to others. I've put together a working implementation\n[here]() against the current master branch. Happy to open a PR for\nreview if the idea makes sense to folks!"
        M3 = "Include full register state in ARM Cortex M Exception Stack Frame (ESF)\n\n**Is your enhancement proposal related to a problem? Please describe.**\n\nTo debug hard-to-reproduce faults/panics, it's helpful to get the full\nregister state at the time the fault occurred. This enables recovering\nfull backtraces and the state of local variables at the time a fault\ntook place.\n\nPretty much all OSs and even some RTOS (i.e mynewt,\nesp-idf) support this in some fashion (i.e coredumps, mini-dumps,\nlinux kernel oops, etc) and it would be awesome if Zephyr could too!\n\nToday this is not possible with the ARM Cortex M Zephyr port for two\nmain reasons:\n\n1). A [copy of the original hardware exception stack\n    frame](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L961-L962)\n    is made before calling k_sys_fatal_error_handler(). This means the\n    stack pointer prior to the exception cannot be recovered making it\n    impossible to recover the full backtrace.\n2). Registers that are callee-saved (r4-r11 & exc_return) are not\n    collected in z_arm_fault() which means when\n    k_sys_fatal_error_handler is called the register state is not\n    readily available. This information is needed to accurately\n    recover local variable state leading up to a crash.\n\n**Describe the solution you'd like**\n\nTo fix these issues and enable better diagnostic facilities, I'd like\nto update the [`z_arch_esf_t` implementation for ARM aarch32](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/include/arch/arm/aarch32/exc.h#L76-L92)\nto pass the original hardware exception frame pointer as well as\ncallee-saved registers.\n\n\n```c\nstruct __full_esf {\n\tstruct __esf *exception_frame;\n\tstruct __callee_saved_esf *callee_regs;\n};\n\ntypedef struct __full_esf z_arch_esf_t;\n```\n\n**Describe alternatives you've considered**\n\nI think there are several different ways the full stack frame could be\nexposed from [z_arm_fault()](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L934-L978). I\ntried to use an approach that would allow the information to be\nexposed via the k_sys_fatal_error_handler API.\n\n**Additional context**\n\nI've been using patches to achieve this behavior on the last few\nZephyr releases but I'd love to upstream the work so it's more\naccessible to others. I've put together a working implementation\n[here]() against the current master branch. Happy to open a PR for\nreview if the idea makes sense to folks!"
        M4 = "Include full register state in ARM Cortex M Exception Stack Frame (ESF)\n\n**Is your enhancement proposal related to a problem? Please describe.**\n\nTo debug hard-to-reproduce faults/panics, it's helpful to get the full\nregister state at the time the fault occurred. This enables recovering\nfull backtraces and the state of local variables at the time a fault\ntook place.\n\nPretty much all OSs and even some RTOS (i.e mynewt,\nesp-idf) support this in some fashion (i.e coredumps, mini-dumps,\nlinux kernel oops, etc) and it would be awesome if Zephyr could too!\n\nToday this is not possible with the ARM Cortex M Zephyr port for two\nmain reasons:\n\n1. A [copy of the original hardware exception stack\nframe](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L961-L962)\nis made before calling k_sys_fatal_error_handler(). This means the\nstack pointer prior to the exception cannot be recovered making it\nimpossible to recover the full backtrace.\n2. Registers that are callee-saved (r4-r11 & exc_return) are not\ncollected in z_arm_fault() which means when k_sys_fatal_error_handler\nis called the register state is not readily available. This\ninformation is needed to accurately recover local variable state\nleading up to a crash.\n\n**Describe the solution you'd like**\n\nTo fix these issues and enable better diagnostic facilities, I'd like\nto update the [`z_arch_esf_t` implementation for ARM aarch32](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/include/arch/arm/aarch32/exc.h#L76-L92)\nto pass the original hardware exception frame pointer as well as\ncallee-saved registers.\n\n\n```c\nstruct __full_esf {\n\tstruct __esf *exception_frame;\n\tstruct __callee_saved_esf *callee_regs;\n};\n\ntypedef struct __full_esf z_arch_esf_t;\n```\n\n**Describe alternatives you've considered**\n\nI think there are several different ways the full stack frame could be\nexposed from [z_arm_fault()](https://github.com/zephyrproject-rtos/zephyr/blob/a1b77fd589dbe7284c17b029f251426a724abd47/arch/arm/core/aarch32/cortex_m/fault.c#L934-L978). I\ntried to use an approach that would allow the information to be\nexposed via the k_sys_fatal_error_handler API.\n\n**Additional context**\n\nI've been using patches to achieve this behavior on the last few\nZephyr releases but I'd love to upstream the work so it's more\naccessible to others. I've put together a working implementation\n[here]() against the current master branch. Happy to open a PR for\nreview if the idea makes sense to folks!"
        proc = GoodMessages(verbose=True)
        proc.commits = [
            {"commit": {"message": M1}},
            {"commit": {"message": M2}},
            {"commit": {"message": M3}},
            {"commit": {"message": M4}},
        ]
        proc.remove_duplicates()
        self.assertEqual(
            [
                {"commit": {"message": M1}},
            ],
            proc.commits
        )

    def test_all_exist_2021_01_01(self):
        # commented ones got lost in word-list updated
        required_shas = [
            "6b997a4e4863f70a9edbb08b8862eb51f4881a1a",
            "13288fe1fc46659dfba59c6ebb0d4fbbffecaf69",
            "cc0766a37555c4850e7fd6bca1d59eb434876f34",
            "1a3368b92e959930b0964f221c9f1f1714f381f7",
            "223ea0b77a736912d0190b2f9996cd4b849f3bbf",
            "3d338278fe58736dd54709dc62feeb508f3d54b6",
            "25b6c6a85897354aaa5b753b203f2e53242b86b7",
            "7106fb7f2df0d5f3216e6f4bb7d48b7a95835509",
            "07e51bdbc7c0630a0a43e85af4fb6bb9798d503f",
            "c595640a344b90965bd080420f7845af65526736",  # not sure
            "2cec9bdcbd1886960fe146d89ca78f0b0b9d790b",  # debatable
            "2aa3e941e84256ea70197e5817425b3db4d546dc",
            "cfa7885777993aeb480dac61d7dd328f908d6cc7",
            #"baf1a2b48e3685137f7d1ba50c56bdddf00bd533",  # debate
            "4fca7cd668b18be9eb7e3ff0169b7dedb62f6b60",
            "27c3fb7ed6cf5fa5a1df986029e3a1e30681cd1d",
            "bd89f4f91082e728cc18b5de2b40f12ba0855a68",
            #"6d7eaa08f4eaad1af358f1a6de699a5238c4a412",
            #"19c87790a190b577ff0bbc78e74cfc723d096c73",
            "aa3d417874450b7418a9792b9667973cf57c624b",
            "badc40d3c22c3b5244360584b8e4c15a756bca38",
            #"aebddd31b8725245e62aa1144bbe5b4490d86392",
            "0dc0c0d08dfda3a79fee2668e3d8fa0acb43a5fa",
            "47090eac17c4c8da34ee29eab181412e73fe88b7",
            "7ee240e6216d3f798f91da65b226cf5911bd02b9",
            "f72402b5fa90ecfb3ac3379f0c61ae2a8d07e8ab",
            #"caaa6010883c8dfc92f0e62ee665887b8a5bc506",  # duplicate?
            "d4bc8476e492e02e3124a794aff394d7535afd36",  # edgy, but should really be there
            "9e91641c01e37ed23e0b29504bfa4d7b4896a0f6",
            "c2dcd81052c32eb5179a20595c7f9c95f7b3d1b5",
            "9093379b39d43902da00c237b1d62a671d2a8eae",
            "853f2299e190d5bfd7898a8ad7c9b0c185655d34",
        ]
        proc = GoodMessages()
        proc.load_stash(STASH_PATH / "2021" / "2021-01-01.json")

        shas = set(c["commit"]["sha"] for c in proc.commits)
        missing_shas = set()
        for required_sha in required_shas:
            if required_sha not in shas:
                missing_shas.add(required_sha)

        self.assertFalse(missing_shas)

        # TODO:
        #   99977cea1c4ab14dbd46866df8711d5a91af16f9 on 2021-12-16
        #       mostly comma separated words should maybe filtered out?
        #   https://github.com/Buildstarted/linksfordevs/commit/9d313e5f0dafbbb138fe3ceaafa6a8d0069e494d
        #       should strip leading <number>. for line comparison