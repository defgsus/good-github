## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-10](docs/good-messages/2022/2022-03-10.md)


1,757,595 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,757,595 were push events containing 2,839,296 commit messages that amount to 203,395,353 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [pedrozzz0/King-Tweaks](https://github.com/pedrozzz0/King-Tweaks)@[7b589961b5...](https://github.com/pedrozzz0/King-Tweaks/commit/7b589961b52cef55951a83f0a6a103d2ff8b922d)
#### Thursday 2022-03-10 00:08:40 by Pedrozzz0

Actually fixup my braindead

* Fuck this shit, man.

Signed-off-by: Pedrozzz0 <guitopzika26@gmail.com>

---
## [hex37/sojourn-station](https://github.com/hex37/sojourn-station)@[83c7559f7c...](https://github.com/hex37/sojourn-station/commit/83c7559f7c9d151b330239652f0b66ba3463584a)
#### Thursday 2022-03-10 00:17:18 by WilliamNelson37

Fratellis and Co

Finishes the Fratellis

Removed Low level code that allowed staff to vore people (why the fuck)

Removed Low level code that allowed staff to regurgitate vored people (god's light has diminished)

---
## [wraiford/ibgib](https://github.com/wraiford/ibgib)@[672a4348b6...](https://github.com/wraiford/ibgib/commit/672a4348b61ee479c6e906dd34ff78feb280954f)
#### Thursday 2022-03-10 00:22:34 by William Raiford

InProgress: sync notifications almost...

* finally got the da*n bubble to show that there was an
  update with sync on!
  * my thinking is incorrect on "turning on sync" vs polling
    for updates.
    * If the user has local sync spaces, we should ask on
      startup if they'd like to connect to their sync spaces,
      or better yet just go ahead and do it and if they cancel
      remember that in ibgibs service.
    * something like that, i'm tired...
* still several bugs to work through regardless
  * when update ibgib happens, it still does not turn back
    on the auto sync (whatever that ends up meaning).
    * I did hack some code to try to avoid this, but I did it
      poorly I guess!
  * there is an updated ibgib error that is happening when I
    hit sync.

---
## [ThongVipPro/Zombi-war](https://github.com/ThongVipPro/Zombi-war)@[b54d1924df...](https://github.com/ThongVipPro/Zombi-war/commit/b54d1924df0b3cc7442feb5644c49b57abd5e219)
#### Thursday 2022-03-10 00:34:53 by Dan Chen

Hey, let me tell you a joke, it's called RUNTIME ERROR! Funny, right? That shit done fucked me up.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[b8ed6f3d79...](https://github.com/san7890/bruhstation/commit/b8ed6f3d797b5a21ebeaf0bcfc30971ebe8598e0)
#### Thursday 2022-03-10 01:30:00 by san7890

Mapper's Delight: Directional Poster Spawners [MDB IGNORE]

A lot of my PRs have been focused on having a fire lit under the seat of my pants. However, this PR is based off one conversation I had with someone.

"Haha, mapper. All you do is var_edits."

It was a bit more verbose than that, but it really did get me thinking about how fucking massive our files our thanks to these var_edits. This PR adds directional helpers to both A) Help mappers map the correct things with as little var edits as possible and B) Lessen the amount of space each fucking map file is thanks to however many extra bytes are taken up with pixel_x = 32. we have a lot of posters.

Bluntly put, this PR adds directional helpers to all generic /random poster spawners. i would add them to every single poster in the game, but that's a lot of work for unique posters, and someone can probably come up with a better idea. Good luck with that, this is just a good first step.

---
## [bluca/systemd-stable](https://github.com/bluca/systemd-stable)@[db1c144c70...](https://github.com/bluca/systemd-stable/commit/db1c144c701a2a5e11b5df768826525c6e2bbaa5)
#### Thursday 2022-03-10 01:36:05 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>
(cherry picked from commit de90700f36f2126528f7ce92df0b5b5d5e277558)
(cherry picked from commit 367041af816d48d4852140f98fd0ba78ed83f9e4)

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[b01bc8250f...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/b01bc8250f189aa627face830a4c3843e54db173)
#### Thursday 2022-03-10 02:01:53 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>

---
## [engine-flutter-autoroll/flutter](https://github.com/engine-flutter-autoroll/flutter)@[99977cea1c...](https://github.com/engine-flutter-autoroll/flutter/commit/99977cea1c4ab14dbd46866df8711d5a91af16f9)
#### Thursday 2022-03-10 02:08:10 by Pierre-Louis

[Fonts] Update icons (#95007)

* update icons

All existing codepoints are stable, with 2 exceptions `wifi_tethering_error_rounded_sharp` and `wifi_tethering_error_rounded_outlined`.

Add 1028 new icons. Codepoints:
airline_seat_individual_suite_baseline, airline_seat_legroom_reduced_baseline, airline_seat_legroom_normal_baseline, airline_seat_recline_normal_baseline, airline_seat_legroom_extra_baseline, airline_seat_recline_extra_baseline, airline_seat_flat_angled_baseline, align_horizontal_center_baseline, account_balance_wallet_baseline, align_horizontal_right_baseline, arrow_drop_down_circle_baseline, airplanemode_inactive_baseline, align_horizontal_left_baseline, align_vertical_bottom_baseline, align_vertical_center_baseline, admin_panel_settings_baseline, assignment_turned_in_baseline, assistant_navigation_baseline, add_photo_alternate_baseline, airplanemode_active_baseline, assignment_returned_baseline, assistant_direction_baseline, auto_awesome_mosaic_baseline, auto_awesome_motion_baseline, access_time_filled_baseline, accessible_forward_baseline, add_circle_outline_baseline, add_to_home_screen_baseline, align_vertical_top_baseline, arrow_back_ios_new_baseline, arrow_circle_right_baseline, arrow_circle_right_outlined, accessibility_new_baseline, add_shopping_cart_baseline, airline_seat_flat_baseline, arrow_circle_down_baseline, arrow_circle_left_baseline, arrow_circle_left_outlined, arrow_circle_right_rounded, arrow_forward_ios_baseline, assignment_return_baseline, add_location_alt_baseline, airplanemode_off_baseline, app_registration_baseline, app_settings_alt_baseline, arrow_circle_left_rounded, assured_workload_baseline, assured_workload_outlined, account_balance_baseline, airplane_ticket_baseline, airplanemode_on_baseline, airport_shuttle_baseline, alternate_email_baseline, arrow_circle_right_sharp, arrow_circle_up_baseline, arrow_drop_down_baseline, arrow_right_alt_baseline, assignment_late_baseline, assistant_photo_baseline, assured_workload_rounded, auto_fix_normal_baseline, account_circle_baseline, arrow_back_ios_baseline, arrow_circle_left_sharp, arrow_downward_baseline, assignment_ind_baseline, autofps_select_baseline, access_alarms_baseline, accessibility_baseline, add_moderator_baseline, add_to_photos_baseline, airline_stops_baseline, airline_stops_outlined, all_inclusive_baseline, arrow_drop_up_baseline, arrow_forward_baseline, assured_workload_sharp, auto_fix_high_baseline, access_alarm_baseline, account_tree_baseline, add_business_baseline, add_location_baseline, add_reaction_baseline, add_to_drive_baseline, add_to_queue_baseline, airline_stops_rounded, announcement_baseline, app_blocking_baseline, app_shortcut_baseline, app_shortcut_outlined, architecture_baseline, arrow_upward_baseline, aspect_ratio_baseline, attach_email_baseline, attach_money_baseline, auto_awesome_baseline, auto_fix_off_baseline, auto_stories_baseline, access_time_baseline, account_box_baseline, add_a_photo_baseline, add_comment_baseline, add_ic_call_baseline, adf_scanner_baseline, adf_scanner_outlined, agriculture_baseline, amp_stories_baseline, app_shortcut_rounded, apps_outage_baseline, apps_outage_outlined, arrow_right_baseline, attach_file_baseline, attractions_baseline, attribution_baseline, auto_delete_baseline, accessible_baseline, add_circle_baseline, adf_scanner_rounded, airline_stops_sharp, apps_outage_rounded, area_chart_baseline, area_chart_outlined, arrow_back_baseline, arrow_left_baseline, assessment_baseline, assignment_baseline, attachment_baseline, audio_file_baseline, audio_file_outlined, audiotrack_baseline, auto_graph_baseline, add_alarm_baseline, add_alert_baseline, add_chart_baseline, ads_click_baseline, ads_click_outlined, alarm_add_baseline, alarm_off_baseline, all_inbox_baseline, alt_route_baseline, analytics_baseline, animation_baseline, apartment_baseline, app_shortcut_sharp, area_chart_rounded, art_track_baseline, assistant_baseline, audio_file_rounded, autorenew_baseline, ad_units_baseline, add_call_baseline, add_card_baseline, add_card_outlined, add_link_baseline, add_road_baseline, add_task_baseline, addchart_baseline, adf_scanner_sharp, ads_click_rounded, airlines_baseline, airlines_outlined, alarm_on_baseline, approval_baseline, apps_outage_sharp, av_timer_baseline, ac_unit_baseline, add_box_baseline, add_card_rounded, airlines_rounded, airplay_baseline, all_out_baseline, android_baseline, archive_baseline, area_chart_sharp, article_baseline, audio_file_sharp, adjust_baseline, ads_click_sharp, anchor_baseline, add_card_sharp, adobe_baseline, adobe_outlined, airlines_sharp, alarm_baseline, album_baseline, apple_baseline, apple_outlined, adobe_rounded, apple_rounded, apps_baseline, abc_baseline, abc_outlined, adb_baseline, add_baseline, air_baseline, aod_baseline, api_baseline, atm_baseline, abc_rounded, adobe_sharp, apple_sharp, abc_sharp, baby_changing_station_baseline, battery_charging_full_baseline, browser_not_supported_baseline, bluetooth_connected_baseline, bluetooth_searching_baseline, bluetooth_disabled_baseline, branding_watermark_baseline, border_horizontal_baseline, brightness_medium_baseline, batch_prediction_baseline, bookmark_outline_baseline, breakfast_dining_baseline, battery_unknown_baseline, bluetooth_audio_baseline, bluetooth_drive_baseline, bookmark_border_baseline, bookmark_remove_baseline, border_vertical_baseline, brightness_auto_baseline, brightness_high_baseline, browser_updated_baseline, browser_updated_outlined, business_center_baseline, bedroom_parent_baseline, bookmark_added_baseline, brightness_low_baseline, browse_gallery_baseline, browse_gallery_outlined, browser_updated_rounded, bakery_dining_baseline, battery_alert_baseline, battery_saver_baseline, bedroom_child_baseline, block_flipped_baseline, blur_circular_baseline, border_bottom_baseline, browse_gallery_rounded, brunch_dining_baseline, backup_table_baseline, battery_full_baseline, beach_access_baseline, bedroom_baby_baseline, bike_scooter_baseline, bookmark_add_baseline, border_clear_baseline, border_color_baseline, border_inner_baseline, border_outer_baseline, border_right_baseline, border_style_baseline, brightness_5_baseline, brightness_4_baseline, brightness_1_baseline, brightness_7_baseline, brightness_6_baseline, brightness_3_baseline, brightness_2_baseline, broken_image_baseline, browser_updated_sharp, bubble_chart_baseline, build_circle_baseline, battery_std_baseline, bedtime_off_baseline, bedtime_off_outlined, blur_linear_baseline, book_online_baseline, border_left_baseline, browse_gallery_sharp, bedtime_off_rounded, border_all_baseline, border_top_baseline, bug_report_baseline, burst_mode_baseline, back_hand_baseline, back_hand_outlined, backspace_baseline, bar_chart_baseline, bloodtype_baseline, bluetooth_baseline, bookmarks_baseline, bus_alert_baseline, back_hand_rounded, backpack_baseline, bathroom_baseline, bedtime_off_sharp, beenhere_baseline, blur_off_baseline, bookmark_baseline, bungalow_baseline, business_baseline, balance_baseline, balance_outlined, balcony_baseline, bathtub_baseline, bedtime_baseline, biotech_baseline, blender_baseline, blur_on_baseline, back_hand_sharp, backup_baseline, balance_rounded, ballot_baseline, badge_baseline, bento_baseline, block_baseline, brush_baseline, build_baseline, balance_sharp, bolt_baseline, book_baseline, bed_baseline, boy_baseline, boy_outlined, boy_rounded, boy_sharp, check_box_outline_blank_baseline, closed_caption_disabled_baseline, connect_without_contact_baseline, control_point_duplicate_baseline, call_missed_outgoing_baseline, cancel_schedule_send_baseline, check_circle_outline_baseline, circle_notifications_baseline, collections_bookmark_baseline, content_paste_search_baseline, content_paste_search_outlined, calendar_view_month_baseline, cancel_presentation_baseline, center_focus_strong_baseline, chat_bubble_outline_baseline, compass_calibration_baseline, confirmation_number_baseline, connecting_airports_baseline, connecting_airports_outlined, content_paste_search_rounded, calendar_view_week_baseline, cast_for_education_baseline, chrome_reader_mode_baseline, closed_caption_off_baseline, connecting_airports_rounded, calendar_view_day_baseline, candlestick_chart_baseline, candlestick_chart_outlined, center_focus_weak_baseline, cleaning_services_baseline, comments_disabled_baseline, comments_disabled_outlined, content_paste_off_baseline, content_paste_search_sharp, create_new_folder_baseline, currency_exchange_baseline, currency_exchange_outlined, candlestick_chart_rounded, catching_pokemon_baseline, charging_station_baseline, close_fullscreen_baseline, comments_disabled_rounded, confirmation_num_baseline, connecting_airports_sharp, content_paste_go_baseline, content_paste_go_outlined, currency_bitcoin_baseline, currency_bitcoin_outlined, currency_exchange_rounded, card_membership_baseline, contact_support_baseline, content_paste_go_rounded, credit_card_off_baseline, currency_bitcoin_rounded, calendar_month_baseline, calendar_month_outlined, calendar_today_baseline, call_to_action_baseline, camera_enhance_baseline, camera_outdoor_baseline, candlestick_chart_sharp, cast_connected_baseline, change_history_baseline, child_friendly_baseline, closed_caption_baseline, cloud_download_baseline, cloudy_snowing_baseline, comments_disabled_sharp, compare_arrows_baseline, control_camera_baseline, corporate_fare_baseline, crop_landscape_baseline, currency_exchange_sharp, currency_franc_baseline, currency_franc_outlined, currency_pound_baseline, currency_pound_outlined, currency_ruble_baseline, currency_ruble_outlined, currency_rupee_baseline, currency_rupee_outlined, calendar_month_rounded, call_received_baseline, camera_indoor_baseline, card_giftcard_baseline, change_circle_baseline, checklist_rtl_baseline, chevron_right_baseline, contact_phone_baseline, content_paste_baseline, content_paste_go_sharp, control_point_baseline, crop_original_baseline, crop_portrait_baseline, currency_bitcoin_sharp, currency_franc_rounded, currency_lira_baseline, currency_lira_outlined, currency_pound_rounded, currency_ruble_rounded, currency_rupee_rounded, currency_yuan_baseline, currency_yuan_outlined, camera_front_baseline, cameraswitch_baseline, check_circle_baseline, chevron_left_baseline, cloud_circle_baseline, cloud_upload_baseline, coffee_maker_baseline, comment_bank_baseline, connected_tv_baseline, construction_baseline, contact_mail_baseline, contact_page_baseline, content_copy_baseline, credit_score_baseline, cruelty_free_baseline, cruelty_free_outlined, currency_lira_rounded, currency_yen_baseline, currency_yen_outlined, currency_yuan_rounded, calendar_month_sharp, call_missed_baseline, camera_rear_baseline, camera_roll_baseline, card_travel_baseline, celebration_baseline, chat_bubble_baseline, clean_hands_baseline, cloud_queue_baseline, collections_baseline, contactless_baseline, content_cut_baseline, coronavirus_baseline, countertops_baseline, credit_card_baseline, crop_rotate_baseline, crop_square_baseline, cruelty_free_rounded, currency_franc_sharp, currency_pound_sharp, currency_ruble_sharp, currency_rupee_sharp, currency_yen_rounded, call_merge_baseline, call_split_baseline, camera_alt_baseline, car_rental_baseline, car_repair_baseline, cell_tower_baseline, cell_tower_outlined, child_care_baseline, cloud_done_baseline, cloud_sync_baseline, cloud_sync_outlined, co_present_baseline, co_present_outlined, color_lens_baseline, currency_lira_sharp, currency_yuan_sharp, calculate_baseline, call_made_baseline, carpenter_baseline, cell_tower_rounded, cell_wifi_baseline, chair_alt_baseline, check_box_baseline, checklist_baseline, checkroom_baseline, clear_all_baseline, cloud_off_baseline, cloud_sync_rounded, co_present_rounded, copyright_baseline, crop_16_9_baseline, crop_free_baseline, cruelty_free_sharp, currency_yen_sharp, call_end_baseline, campaign_baseline, category_baseline, code_off_baseline, colorize_baseline, compress_baseline, computer_baseline, contacts_baseline, contrast_baseline, contrast_outlined, copy_all_baseline, crop_din_baseline, crop_5_4_baseline, crop_7_5_baseline, crop_3_2_baseline, cell_tower_sharp, cloud_sync_sharp, co_present_sharp, comment_baseline, commute_baseline, compare_baseline, compost_baseline, compost_outlined, contrast_rounded, cottage_baseline, cached_baseline, camera_baseline, cancel_baseline, casino_baseline, castle_baseline, castle_outlined, chalet_baseline, church_baseline, church_outlined, circle_baseline, coffee_baseline, commit_baseline, commit_outlined, compost_rounded, cookie_baseline, cookie_outlined, create_baseline, cabin_baseline, cable_baseline, cases_baseline, castle_rounded, chair_baseline, check_baseline, church_rounded, class_baseline, clear_baseline, close_baseline, cloud_baseline, commit_rounded, contrast_sharp, cookie_rounded, cake_baseline, call_baseline, cast_baseline, chat_baseline, code_baseline, compost_sharp, copy_baseline, crib_baseline, crop_baseline, castle_sharp, church_sharp, co2_baseline, co2_outlined, commit_sharp, cookie_sharp, css_baseline, css_outlined, cut_baseline, co2_rounded, css_rounded, co2_sharp, css_sharp, do_not_disturb_on_total_silence_baseline, directions_railway_filled_baseline, directions_transit_filled_baseline, drive_file_rename_outline_baseline, directions_subway_filled_baseline, desktop_access_disabled_baseline, drive_file_move_outline_baseline, directions_boat_filled_baseline, directions_bus_filled_baseline, directions_car_filled_baseline, download_for_offline_baseline, dashboard_customize_baseline, developer_board_off_baseline, disabled_by_default_baseline, domain_verification_baseline, drive_file_move_rtl_baseline, drive_file_move_rtl_outlined, drive_folder_upload_baseline, directions_railway_baseline, directions_transit_baseline, do_not_disturb_alt_baseline, do_not_disturb_off_baseline, drive_file_move_rtl_rounded, data_thresholding_baseline, data_thresholding_outlined, device_thermostat_baseline, directions_subway_baseline, do_not_disturb_on_baseline, data_exploration_baseline, data_exploration_outlined, data_thresholding_rounded, directions_ferry_baseline, directions_train_baseline, disabled_visible_baseline, disabled_visible_outlined, display_settings_baseline, display_settings_outlined, dnd_forwardslash_baseline, document_scanner_baseline, drive_file_move_rtl_sharp, data_exploration_rounded, delivery_dining_baseline, departure_board_baseline, design_services_baseline, desktop_windows_baseline, developer_board_baseline, directions_bike_baseline, directions_boat_baseline, directions_walk_baseline, disabled_visible_rounded, display_settings_rounded, domain_disabled_baseline, downhill_skiing_baseline, drive_file_move_baseline, data_saver_off_baseline, data_thresholding_sharp, delete_forever_baseline, delete_outline_baseline, density_medium_baseline, density_medium_outlined, developer_mode_baseline, device_unknown_baseline, directions_bus_baseline, directions_car_baseline, directions_off_baseline, directions_run_baseline, do_disturb_alt_baseline, do_disturb_off_baseline, do_not_disturb_baseline, drag_indicator_baseline, data_exploration_sharp, data_saver_on_baseline, density_large_baseline, density_large_outlined, density_medium_rounded, density_small_baseline, density_small_outlined, devices_other_baseline, dinner_dining_baseline, disabled_visible_sharp, display_settings_sharp, do_disturb_on_baseline, download_done_baseline, delete_sweep_baseline, density_large_rounded, density_small_rounded, do_not_touch_baseline, done_outline_baseline, door_sliding_baseline, double_arrow_baseline, dry_cleaning_baseline, dynamic_feed_baseline, dynamic_form_baseline, data_object_baseline, data_object_outlined, density_medium_sharp, description_baseline, desktop_mac_baseline, do_not_step_baseline, donut_large_baseline, donut_small_baseline, downloading_baseline, drag_handle_baseline, data_array_baseline, data_array_outlined, data_object_rounded, data_usage_baseline, date_range_baseline, density_large_sharp, density_small_sharp, device_hub_baseline, dialer_sip_baseline, difference_baseline, difference_outlined, directions_baseline, dirty_lens_baseline, do_disturb_baseline, domain_add_baseline, domain_add_outlined, door_front_baseline, dangerous_baseline, dark_mode_baseline, dashboard_baseline, data_array_rounded, difference_rounded, disc_full_baseline, domain_add_rounded, door_back_baseline, drive_eta_baseline, data_object_sharp, deselect_baseline, deselect_outlined, discount_baseline, discount_outlined, done_all_baseline, doorbell_baseline, download_baseline, data_array_sharp, deselect_rounded, details_baseline, devices_baseline, dialpad_baseline, diamond_baseline, diamond_outlined, difference_sharp, discord_baseline, discord_outlined, discount_rounded, domain_add_sharp, deblur_baseline, deblur_outlined, dehaze_baseline, delete_baseline, diamond_rounded, dining_baseline, discord_rounded, domain_baseline, drafts_baseline, deblur_rounded, deselect_sharp, discount_sharp, deck_baseline, diamond_sharp, discord_sharp, dock_baseline, done_baseline, draw_baseline, draw_outlined, deblur_sharp, dns_baseline, draw_rounded, dry_baseline, duo_baseline, dvr_baseline, draw_sharp, 4g_plus_mobiledata_baseline, 4g_mobiledata_baseline, 4k_plus_baseline, 4mp_baseline, 4k_baseline, 5k_plus_baseline, 5mp_baseline, 5g_baseline, 5k_baseline, 8k_plus_baseline, 8mp_baseline, 8k_baseline, 1x_mobiledata_baseline, 1k_plus_baseline, 18mp_baseline, 15mp_baseline, 14mp_baseline, 19mp_baseline, 11mp_baseline, 17mp_baseline, 16mp_baseline, 13mp_baseline, 12mp_baseline, 10mp_baseline, 123_baseline, 123_outlined, 10k_baseline, 123_rounded, 1k_baseline, 123_sharp, enhance_photo_translate_baseline, emoji_transportation_baseline, electrical_services_baseline, emoji_food_beverage_baseline, enhanced_encryption_baseline, edit_notifications_baseline, expand_circle_down_baseline, expand_circle_down_outlined, edit_location_alt_baseline, electric_rickshaw_baseline, escalator_warning_baseline, expand_circle_down_rounded, electric_scooter_baseline, exposure_minus_1_baseline, exposure_minus_2_baseline, earbuds_battery_baseline, edgesensor_high_baseline, edit_attributes_baseline, event_available_baseline, expand_circle_down_sharp, exposure_plus_1_baseline, exposure_plus_2_baseline, edgesensor_low_baseline, electric_moped_baseline, emoji_emotions_baseline, exposure_neg_1_baseline, exposure_neg_2_baseline, edit_calendar_baseline, edit_calendar_outlined, edit_location_baseline, elderly_woman_baseline, elderly_woman_outlined, electric_bike_baseline, emoji_objects_baseline, emoji_symbols_baseline, error_outline_baseline, exposure_zero_baseline, extension_off_baseline, e_mobiledata_baseline, edit_calendar_rounded, elderly_woman_rounded, electric_car_baseline, emoji_events_baseline, emoji_nature_baseline, emoji_people_baseline, event_repeat_baseline, event_repeat_outlined, emoji_flags_baseline, engineering_baseline, euro_symbol_baseline, event_repeat_rounded, exit_to_app_baseline, expand_less_baseline, expand_more_baseline, explore_off_baseline, edit_calendar_sharp, elderly_woman_sharp, ev_station_baseline, event_busy_baseline, event_note_baseline, event_seat_baseline, edit_note_baseline, edit_note_outlined, edit_road_baseline, emergency_baseline, emergency_outlined, equalizer_baseline, escalator_baseline, event_repeat_sharp, extension_baseline, edit_note_rounded, edit_off_baseline, elevator_baseline, emergency_rounded, explicit_baseline, exposure_baseline, earbuds_baseline, egg_alt_baseline, egg_alt_outlined, elderly_baseline, explore_baseline, edit_note_sharp, egg_alt_rounded, emergency_sharp, expand_baseline, eject_baseline, email_baseline, error_baseline, event_baseline, east_baseline, edit_baseline, egg_alt_sharp, euro_baseline, eco_baseline, egg_baseline, egg_outlined, egg_rounded, egg_sharp, 2k_plus_baseline, 24mp_baseline, 21mp_baseline, 23mp_baseline, 22mp_baseline, 20mp_baseline, 2mp_baseline, 2k_baseline, 3g_mobiledata_baseline, 30fps_select_baseline, 3d_rotation_baseline, 3k_plus_baseline, 30fps_baseline, 360_baseline, 3mp_baseline, 3k_baseline, 3p_baseline, 60fps_select_baseline, 6_ft_apart_baseline, 6k_plus_baseline, 60fps_baseline, 6mp_baseline, 6k_baseline, 7k_plus_baseline, 7mp_baseline, 7k_baseline, 9k_plus_baseline, 9mp_baseline, 9k_baseline, format_textdirection_l_to_r_baseline, format_textdirection_r_to_l_baseline, format_list_numbered_rtl_baseline, face_retouching_natural_baseline, format_indent_decrease_baseline, format_indent_increase_baseline, format_align_justify_baseline, format_list_bulleted_baseline, format_list_numbered_baseline, format_strikethrough_baseline, face_retouching_off_baseline, fiber_manual_record_baseline, filter_center_focus_baseline, flip_camera_android_baseline, format_align_center_baseline, format_line_spacing_baseline, featured_play_list_baseline, fiber_smart_record_baseline, file_download_done_baseline, format_align_right_baseline, format_color_reset_baseline, file_download_off_baseline, filter_tilt_shift_baseline, fire_extinguisher_baseline, font_download_off_baseline, format_align_left_baseline, format_color_fill_baseline, format_color_text_baseline, format_underlined_baseline, free_cancellation_baseline, free_cancellation_outlined, favorite_outline_baseline, follow_the_signs_baseline, format_underline_baseline, forward_to_inbox_baseline, free_cancellation_rounded, family_restroom_baseline, favorite_border_baseline, filter_list_alt_baseline, filter_list_off_baseline, filter_list_off_outlined, flip_camera_ios_baseline, format_overline_baseline, format_overline_outlined, fullscreen_exit_baseline, featured_video_baseline, filter_alt_off_baseline, filter_alt_off_outlined, filter_b_and_w_baseline, filter_list_off_rounded, filter_vintage_baseline, fitness_center_baseline, flashlight_off_baseline, flight_takeoff_baseline, folder_special_baseline, format_overline_rounded, free_breakfast_baseline, free_cancellation_sharp, file_download_baseline, filter_alt_off_rounded, filter_9_plus_baseline, filter_frames_baseline, flashlight_on_baseline, flip_to_front_baseline, folder_delete_baseline, folder_delete_outlined, folder_shared_baseline, font_download_baseline, format_italic_baseline, format_shapes_baseline, fast_forward_baseline, file_present_baseline, filter_drama_baseline, filter_list_off_sharp, find_in_page_baseline, find_replace_baseline, fire_hydrant_baseline, flight_class_baseline, flight_class_outlined, flip_to_back_baseline, flutter_dash_baseline, folder_delete_rounded, format_clear_baseline, format_overline_sharp, format_paint_baseline, format_quote_baseline, fast_rewind_baseline, file_upload_baseline, filter_alt_off_sharp, filter_list_baseline, filter_none_baseline, fingerprint_baseline, flag_circle_baseline, flag_circle_outlined, flight_class_rounded, flight_land_baseline, flourescent_baseline, folder_copy_baseline, folder_copy_outlined, folder_open_baseline, format_bold_baseline, format_size_baseline, fact_check_baseline, filter_alt_baseline, filter_hdr_baseline, first_page_baseline, fit_screen_baseline, flag_circle_rounded, flash_auto_baseline, folder_copy_rounded, folder_delete_sharp, folder_off_baseline, folder_off_outlined, folder_zip_baseline, folder_zip_outlined, fork_right_baseline, fork_right_outlined, forward_10_baseline, forward_30_baseline, foundation_baseline, front_hand_baseline, front_hand_outlined, fullscreen_baseline, fiber_dvr_baseline, fiber_new_baseline, fiber_pin_baseline, file_copy_baseline, file_open_baseline, file_open_outlined, fireplace_baseline, flash_off_baseline, flight_class_sharp, folder_off_rounded, folder_zip_rounded, food_bank_baseline, fork_left_baseline, fork_left_outlined, fork_right_rounded, forward_5_baseline, front_hand_rounded, functions_baseline, facebook_baseline, fastfood_baseline, favorite_baseline, feedback_baseline, festival_baseline, file_open_rounded, filter_8_baseline, filter_5_baseline, filter_4_baseline, filter_9_baseline, filter_1_baseline, filter_7_baseline, filter_6_baseline, filter_3_baseline, filter_2_baseline, flag_circle_sharp, flash_on_baseline, flatware_baseline, fmd_good_baseline, folder_copy_sharp, fork_left_rounded, factory_baseline, factory_outlined, fmd_bad_baseline, folder_off_sharp, folder_zip_sharp, fork_right_sharp, forward_baseline, front_hand_sharp, factory_rounded, female_baseline, file_open_sharp, filter_baseline, fitbit_baseline, fitbit_outlined, flight_baseline, folder_baseline, forest_baseline, forest_outlined, fork_left_sharp, fence_baseline, fitbit_rounded, flaky_baseline, flare_baseline, foggy_baseline, forest_rounded, forum_baseline, face_baseline, factory_sharp, feed_baseline, flag_baseline, flip_baseline, fort_baseline, fort_outlined, fax_baseline, fax_outlined, fitbit_sharp, forest_sharp, fort_rounded, fax_rounded, fort_sharp, fax_sharp, generating_tokens_baseline, generating_tokens_outlined, generating_tokens_rounded, grid_goldenratio_baseline, generating_tokens_sharp, gps_not_fixed_baseline, g_mobiledata_baseline, group_remove_baseline, group_remove_outlined, g_translate_baseline, golf_course_baseline, group_remove_rounded, graphic_eq_baseline, group_work_baseline, gpp_maybe_baseline, gps_fixed_baseline, grid_view_baseline, group_add_baseline, group_off_baseline, group_off_outlined, group_remove_sharp, gpp_good_baseline, gradient_baseline, grid_4x4_baseline, grid_3x3_baseline, grid_off_baseline, group_off_rounded, gamepad_baseline, gesture_baseline, get_app_baseline, gif_box_baseline, gif_box_outlined, gpp_bad_baseline, gps_off_baseline, grading_baseline, grid_on_baseline, garage_baseline, gif_box_rounded, group_off_sharp, groups_baseline, games_baseline, gavel_baseline, grade_baseline, grain_baseline, grass_baseline, group_baseline, gif_box_sharp, girl_baseline, girl_outlined, gite_baseline, gif_baseline, girl_rounded, girl_sharp, horizontal_distribute_baseline, hdr_enhanced_select_baseline, home_repair_service_baseline, headphones_battery_baseline, history_toggle_off_baseline, hourglass_disabled_baseline, h_plus_mobiledata_baseline, health_and_safety_baseline, hearing_disabled_baseline, highlight_remove_baseline, horizontal_split_baseline, hourglass_bottom_baseline, hdr_auto_select_baseline, holiday_village_baseline, horizontal_rule_baseline, hourglass_empty_baseline, hdr_off_select_baseline, hourglass_full_baseline, hdr_on_select_baseline, highlight_alt_baseline, highlight_off_baseline, hourglass_top_baseline, h_mobiledata_baseline, heart_broken_baseline, heart_broken_outlined, help_outline_baseline, high_quality_baseline, house_siding_baseline, headset_mic_baseline, headset_off_baseline, heart_broken_rounded, help_center_baseline, hide_source_baseline, history_edu_baseline, home_filled_baseline, hotel_class_baseline, hotel_class_outlined, how_to_vote_baseline, hdr_strong_baseline, headphones_baseline, hide_image_baseline, hotel_class_rounded, how_to_reg_baseline, handshake_baseline, handshake_outlined, heart_broken_sharp, highlight_baseline, home_mini_baseline, home_work_baseline, houseboat_baseline, handshake_rounded, handyman_baseline, hardware_baseline, hdr_auto_baseline, hdr_plus_baseline, hdr_weak_baseline, home_max_baseline, hotel_class_sharp, hdr_off_baseline, headset_baseline, healing_baseline, hearing_baseline, hexagon_baseline, hexagon_outlined, history_baseline, hls_off_baseline, hls_off_outlined, hot_tub_baseline, handshake_sharp, hdr_on_baseline, height_baseline, hexagon_rounded, hiking_baseline, hls_off_rounded, hotel_baseline, house_baseline, https_baseline, hail_baseline, help_baseline, hevc_baseline, hexagon_sharp, hive_baseline, hive_outlined, hls_off_sharp, home_baseline, html_baseline, html_outlined, http_baseline, hvac_baseline, hive_rounded, hls_baseline, hls_outlined, html_rounded, hub_baseline, hub_outlined, hd_baseline, hls_rounded, hub_rounded, hive_sharp, html_sharp, hls_sharp, hub_sharp, keyboard_double_arrow_right_baseline, keyboard_double_arrow_right_outlined, keyboard_double_arrow_down_baseline, keyboard_double_arrow_down_outlined, keyboard_double_arrow_left_baseline, keyboard_double_arrow_left_outlined, keyboard_double_arrow_right_rounded, keyboard_double_arrow_down_rounded, keyboard_double_arrow_left_rounded, keyboard_double_arrow_right_sharp, keyboard_double_arrow_up_baseline, keyboard_double_arrow_up_outlined, keyboard_double_arrow_down_sharp, keyboard_double_arrow_left_sharp, keyboard_double_arrow_up_rounded, keyboard_double_arrow_up_sharp, keyboard_arrow_right_baseline, keyboard_command_key_baseline, keyboard_command_key_outlined, keyboard_control_key_baseline, keyboard_control_key_outlined, keyboard_arrow_down_baseline, keyboard_arrow_left_baseline, keyboard_command_key_rounded, keyboard_control_key_rounded, keyboard_option_key_baseline, keyboard_option_key_outlined, keyboard_backspace_baseline, keyboard_option_key_rounded, keyboard_arrow_up_baseline, keyboard_capslock_baseline, keyboard_command_key_sharp, keyboard_control_key_sharp, keyboard_control_baseline, keyboard_option_key_sharp, keyboard_return_baseline, keyboard_voice_baseline, keyboard_hide_baseline, kebab_dining_baseline, kebab_dining_outlined, keyboard_alt_baseline, keyboard_tab_baseline, kebab_dining_rounded, kitesurfing_baseline, kebab_dining_sharp, kayaking_baseline, keyboard_baseline, king_bed_baseline, key_off_baseline, key_off_outlined, kitchen_baseline, key_off_rounded, key_off_sharp, key_baseline, key_outlined, key_rounded, key_sharp, label_important_outline_baseline, local_convenience_store_baseline, local_fire_department_baseline, local_laundry_service_baseline, local_grocery_store_baseline, lte_plus_mobiledata_baseline, leave_bags_at_home_baseline, location_searching_baseline, laptop_chromebook_baseline, library_add_check_baseline, lightbulb_outline_baseline, local_gas_station_baseline, local_post_office_baseline, location_disabled_baseline, local_attraction_baseline, local_print_shop_baseline, local_restaurant_baseline, location_history_baseline, label_important_baseline, local_printshop_baseline, laptop_windows_baseline, local_activity_baseline, local_car_wash_baseline, local_hospital_baseline, local_pharmacy_baseline, local_shipping_baseline, lte_mobiledata_baseline, label_outline_baseline, legend_toggle_baseline, library_books_baseline, library_music_baseline, linked_camera_baseline, local_airport_baseline, local_florist_baseline, local_library_baseline, local_parking_baseline, location_city_baseline, layers_clear_baseline, linear_scale_baseline, local_dining_baseline, local_movies_baseline, local_police_baseline, location_off_baseline, location_pin_baseline, lock_outline_baseline, low_priority_baseline, lunch_dining_baseline, leaderboard_baseline, leak_remove_baseline, library_add_baseline, line_weight_baseline, local_drink_baseline, local_hotel_baseline, local_offer_baseline, local_phone_baseline, local_pizza_baseline, location_on_baseline, laptop_mac_baseline, light_mode_baseline, line_style_baseline, local_cafe_baseline, local_mall_baseline, local_play_baseline, local_taxi_baseline, lock_clock_baseline, lock_reset_baseline, lock_reset_outlined, label_off_baseline, landscape_baseline, last_page_baseline, lens_blur_baseline, lightbulb_baseline, line_axis_baseline, line_axis_outlined, live_help_baseline, local_atm_baseline, local_bar_baseline, local_see_baseline, lock_open_baseline, lock_reset_rounded, looks_one_baseline, looks_two_baseline, language_baseline, leak_add_baseline, line_axis_rounded, link_off_baseline, list_alt_baseline, logo_dev_baseline, logo_dev_outlined, live_tv_baseline, lock_reset_sharp, logo_dev_rounded, looks_5_baseline, looks_4_baseline, looks_6_baseline, looks_3_baseline, loyalty_baseline, luggage_baseline, laptop_baseline, launch_baseline, layers_baseline, line_axis_sharp, liquor_baseline, living_baseline, logout_baseline, label_baseline, light_baseline, login_baseline, logo_dev_sharp, looks_baseline, loupe_baseline, lens_baseline, link_baseline, list_baseline, lock_baseline, loop_baseline, lan_baseline, lan_outlined, lan_rounded, lan_sharp, integration_instructions_baseline, indeterminate_check_box_baseline, insert_chart_outlined_baseline, image_not_supported_baseline, image_aspect_ratio_baseline, imagesearch_roller_baseline, important_devices_baseline, incomplete_circle_baseline, incomplete_circle_outlined, insert_drive_file_baseline, insert_invitation_baseline, insert_page_break_baseline, insert_page_break_outlined, invert_colors_off_baseline, incomplete_circle_rounded, insert_page_break_rounded, interpreter_mode_baseline, interpreter_mode_outlined, invert_colors_on_baseline, import_contacts_baseline, insert_emoticon_baseline, install_desktop_baseline, install_desktop_outlined, interpreter_mode_rounded, incomplete_circle_sharp, insert_comment_baseline, insert_page_break_sharp, install_desktop_rounded, install_mobile_baseline, install_mobile_outlined, import_export_baseline, install_mobile_rounded, interpreter_mode_sharp, invert_colors_baseline, image_search_baseline, info_outline_baseline, insert_chart_baseline, insert_photo_baseline, install_desktop_sharp, ice_skating_baseline, insert_link_baseline, install_mobile_sharp, inventory_2_baseline, interests_baseline, interests_outlined, inventory_baseline, ios_share_baseline, icecream_baseline, insights_baseline, interests_rounded, interests_sharp, image_baseline, inbox_baseline, input_baseline, info_baseline, iron_baseline, iso_baseline, javascript_baseline, javascript_outlined, join_inner_baseline, join_inner_outlined, join_right_baseline, join_right_outlined, javascript_rounded, join_full_baseline, join_full_outlined, join_inner_rounded, join_left_baseline, join_left_outlined, join_right_rounded, join_full_rounded, join_left_rounded, javascript_sharp, join_inner_sharp, join_right_sharp, join_full_sharp, join_left_sharp, online_prediction_baseline, open_in_browser_baseline, open_in_new_off_baseline, ondemand_video_baseline, offline_share_baseline, outdoor_grill_baseline, outgoing_mail_baseline, outlined_flag_baseline, offline_bolt_baseline, open_in_full_baseline, other_houses_baseline, offline_pin_baseline, open_in_new_baseline, open_with_baseline, outbound_baseline, opacity_baseline, outbond_baseline, outbox_baseline, outlet_baseline, output_baseline, output_outlined, output_rounded, output_sharp, no_encryption_gmailerrorred_baseline, notification_important_baseline, notifications_active_baseline, notifications_paused_baseline, not_listed_location_baseline, notifications_none_baseline, notifications_off_baseline, near_me_disabled_baseline, nightlight_round_baseline, notification_add_baseline, notifications_on_baseline, navigate_before_baseline, no_meals_ouline_baseline, no_meeting_room_baseline, network_locked_baseline, no_photography_baseline, nordic_walking_baseline, not_accessible_baseline, not_interested_baseline, nature_people_baseline, navigate_next_baseline, network_check_baseline, night_shelter_baseline, no_encryption_baseline, notifications_baseline, now_wallpaper_baseline, nearby_error_baseline, network_cell_baseline, network_ping_baseline, network_ping_outlined, network_wifi_baseline, new_releases_baseline, network_ping_rounded, nights_stay_baseline, no_accounts_baseline, no_backpack_baseline, no_stroller_baseline, no_transfer_baseline, not_started_baseline, now_widgets_baseline, navigation_baseline, nearby_off_baseline, nightlight_baseline, no_luggage_baseline, north_east_baseline, north_west_baseline, network_ping_sharp, new_label_baseline, newspaper_baseline, newspaper_outlined, next_plan_baseline, next_week_baseline, nightlife_baseline, no_drinks_baseline, newspaper_rounded, no_flash_baseline, no_meals_baseline, note_add_baseline, note_alt_baseline, near_me_baseline, no_cell_baseline, no_food_baseline, numbers_baseline, numbers_outlined, nature_baseline, newspaper_sharp, no_sim_baseline, numbers_rounded, north_baseline, notes_baseline, note_baseline, numbers_sharp, nat_baseline, nfc_baseline, miscellaneous_services_baseline, mark_unread_chat_alt_baseline, mark_unread_chat_alt_outlined, motion_photos_paused_baseline, mark_unread_chat_alt_rounded, media_bluetooth_off_baseline, mobile_screen_share_baseline, motion_photos_pause_baseline, markunread_mailbox_baseline, media_bluetooth_on_baseline, motion_photos_auto_baseline, mark_email_unread_baseline, mark_unread_chat_alt_sharp, medication_liquid_baseline, medication_liquid_outlined, messenger_outline_baseline, missed_video_call_baseline, mode_edit_outline_baseline, monochrome_photos_baseline, motion_photos_off_baseline, mark_chat_unread_baseline, medical_services_baseline, medication_liquid_rounded, mic_external_off_baseline, motion_photos_on_baseline, multitrack_audio_baseline, my_library_books_baseline, my_library_music_baseline, manage_accounts_baseline, mark_email_read_baseline, mic_external_on_baseline, mobile_friendly_baseline, monetization_on_baseline, money_off_csred_baseline, multiline_chart_baseline, maps_home_work_baseline, mark_as_unread_baseline, mark_chat_read_baseline, medication_liquid_sharp, mobiledata_off_baseline, mode_of_travel_baseline, mode_of_travel_outlined, model_training_baseline, monitor_weight_baseline, movie_creation_baseline, my_library_add_baseline, manage_search_baseline, military_tech_baseline, mode_of_travel_rounded, monitor_heart_baseline, monitor_heart_outlined, move_to_inbox_baseline, multiple_stop_baseline, mail_outline_baseline, meeting_room_baseline, mode_comment_baseline, mode_standby_baseline, monitor_heart_rounded, movie_filter_baseline, mode_of_travel_sharp, music_video_baseline, my_location_baseline, markunread_baseline, medication_baseline, merge_type_baseline, mobile_off_baseline, mode_night_baseline, monitor_heart_sharp, more_horiz_baseline, motorcycle_baseline, music_note_baseline, mediation_baseline, menu_book_baseline, menu_open_baseline, messenger_baseline, microwave_baseline, mode_edit_baseline, money_off_baseline, more_time_baseline, more_vert_baseline, move_down_baseline, move_down_outlined, music_off_baseline, maps_ugc_baseline, maximize_baseline, mic_none_baseline, minimize_baseline, mood_bad_baseline, move_down_rounded, message_baseline, mic_off_baseline, monitor_baseline, move_up_baseline, move_up_outlined, margin_baseline, memory_baseline, mosque_baseline, mosque_outlined, move_down_sharp, move_up_rounded, moving_baseline, museum_baseline, masks_baseline, merge_baseline, merge_outlined, money_baseline, moped_baseline, mosque_rounded, mouse_baseline, movie_baseline, mail_baseline, male_baseline, menu_baseline, merge_rounded, mode_baseline, mood_baseline, more_baseline, move_up_sharp, man_baseline, man_outlined, map_baseline, mic_baseline, mms_baseline, mosque_sharp, man_rounded, merge_sharp, mp_baseline, man_sharp, panorama_photosphere_select_baseline, panorama_horizontal_select_baseline, panorama_wide_angle_select_baseline, production_quantity_limits_baseline, playlist_add_check_circle_baseline, playlist_add_check_circle_outlined, panorama_vertical_select_baseline, photo_size_select_actual_baseline, playlist_add_check_circle_rounded, perm_device_information_baseline, phone_bluetooth_speaker_baseline, photo_size_select_large_baseline, photo_size_select_small_baseline, precision_manufacturing_baseline, picture_in_picture_alt_baseline, playlist_add_check_circle_sharp, published_with_changes_baseline, perm_contact_calendar_baseline, panorama_photosphere_baseline, pause_circle_outline_baseline, private_connectivity_baseline, private_connectivity_outlined, panorama_horizontal_baseline, panorama_wide_angle_baseline, pause_circle_filled_baseline, person_add_disabled_baseline, person_remove_alt_1_baseline, pest_control_rodent_baseline, play_circle_outline_baseline, playlist_add_circle_baseline, playlist_add_circle_outlined, private_connectivity_rounded, pause_presentation_baseline, photo_camera_front_baseline, picture_in_picture_baseline, play_circle_filled_baseline, playlist_add_check_baseline, playlist_add_circle_rounded, power_settings_new_baseline, panorama_fish_eye_baseline, panorama_vertical_baseline, perm_data_setting_baseline, person_pin_circle_baseline, photo_camera_back_baseline, pie_chart_outline_baseline, pivot_table_chart_baseline, portable_wifi_off_baseline, private_connectivity_sharp, panorama_fisheye_baseline, perm_contact_cal_baseline, perm_device_info_baseline, person_add_alt_1_baseline, play_circle_fill_baseline, playlist_add_circle_sharp, pending_actions_baseline, perm_camera_mic_baseline, personal_injury_baseline, phone_forwarded_baseline, phonelink_erase_baseline, phonelink_setup_baseline, playlist_remove_baseline, playlist_remove_outlined, people_outline_baseline, perm_phone_msg_baseline, perm_scan_wifi_baseline, person_add_alt_baseline, person_outline_baseline, personal_video_baseline, phone_callback_baseline, phone_disabled_baseline, phonelink_lock_baseline, phonelink_ring_baseline, picture_as_pdf_baseline, playlist_remove_rounded, pregnant_woman_baseline, present_to_all_baseline, print_disabled_baseline, perm_identity_baseline, person_remove_baseline, person_search_baseline, phone_android_baseline, phone_enabled_baseline, phone_in_talk_baseline, phonelink_off_baseline, photo_library_baseline, play_disabled_baseline, play_for_work_baseline, playlist_play_baseline, point_of_sale_baseline, priority_high_baseline, pan_tool_alt_baseline, pan_tool_alt_outlined, pause_circle_baseline, pest_control_baseline, phone_iphone_baseline, phone_locked_baseline, phone_missed_baseline, phone_paused_baseline, photo_camera_baseline, photo_filter_baseline, playlist_add_baseline, playlist_remove_sharp, price_change_baseline, pan_tool_alt_rounded, paragliding_baseline, photo_album_baseline, play_circle_baseline, play_lesson_baseline, power_input_baseline, price_check_baseline, privacy_tip_baseline, punch_clock_baseline, punch_clock_outlined, party_mode_baseline, pedal_bike_baseline, people_alt_baseline, perm_media_baseline, person_add_baseline, person_off_baseline, person_pin_baseline, pin_invoke_baseline, pin_invoke_outlined, plagiarism_baseline, play_arrow_baseline, psychology_baseline, public_off_baseline, punch_clock_rounded, pan_tool_alt_sharp, phonelink_baseline, piano_off_baseline, pie_chart_baseline, pin_invoke_rounded, power_off_baseline, pageview_baseline, pan_tool_baseline, panorama_baseline, password_baseline, payments_baseline, pentagon_baseline, pentagon_outlined, phishing_baseline, phishing_outlined, pin_drop_baseline, plumbing_baseline, plus_one_baseline, podcasts_baseline, polyline_baseline, polyline_outlined, portrait_baseline, post_add_baseline, punch_clock_sharp, push_pin_baseline, padding_baseline, palette_baseline, pattern_baseline, payment_baseline, pending_baseline, pentagon_rounded, percent_baseline, percent_outlined, phishing_rounded, pin_end_baseline, pin_end_outlined, pin_invoke_sharp, polyline_rounded, polymer_baseline, preview_baseline, publish_baseline, paypal_baseline, paypal_outlined, people_baseline, percent_rounded, person_baseline, pin_end_rounded, policy_baseline, public_baseline, pages_baseline, paste_baseline, pause_baseline, paypal_rounded, pentagon_sharp, phishing_sharp, phone_baseline, photo_baseline, piano_baseline, pinch_baseline, pinch_outlined, place_baseline, polyline_sharp, power_baseline, print_baseline, paid_baseline, park_baseline, percent_sharp, pets_baseline, pin_end_sharp, pinch_rounded, poll_baseline, pool_baseline, paypal_sharp, php_baseline, php_outlined, pin_baseline, pix_baseline, pix_outlined, php_rounded, pinch_sharp, pix_rounded, php_sharp, pix_sharp, quick_contacts_dialer_baseline, quick_contacts_mail_baseline, qr_code_scanner_baseline, question_answer_baseline, queue_play_next_baseline, query_builder_baseline, question_mark_baseline, question_mark_outlined, question_mark_rounded, query_stats_baseline, queue_music_baseline, question_mark_sharp, quickreply_baseline, qr_code_2_baseline, qr_code_baseline, queue_baseline, quora_baseline, quora_outlined, quiz_baseline, quora_rounded, quora_sharp, signal_wifi_statusbar_connected_no_internet_4_baseline, signal_cellular_connected_no_internet_4_bar_baseline, signal_cellular_connected_no_internet_0_bar_baseline, signal_wifi_connected_no_internet_4_baseline, sentiment_very_dissatisfied_baseline, signal_wifi_statusbar_4_bar_baseline, signal_wifi_statusbar_null_baseline, sentiment_very_satisfied_baseline, settings_input_component_baseline, settings_input_composite_baseline, settings_system_daydream_baseline, subdirectory_arrow_right_baseline, security_update_warning_baseline, sentiment_satisfied_alt_baseline, settings_backup_restore_baseline, subdirectory_arrow_left_baseline, sentiment_dissatisfied_baseline, settings_accessibility_baseline, settings_input_antenna_baseline, shopping_cart_checkout_baseline, shopping_cart_checkout_outlined, signal_cellular_no_sim_baseline, signal_cellular_nodata_baseline, signal_wifi_4_bar_lock_baseline, stay_current_landscape_baseline, stay_primary_landscape_baseline, screen_lock_landscape_baseline, screen_search_desktop_baseline, settings_applications_baseline, settings_input_svideo_baseline, shopping_cart_checkout_rounded, signal_cellular_4_bar_baseline, signal_cellular_0_bar_baseline, star_border_purple500_baseline, stay_current_portrait_baseline, stay_primary_portrait_baseline, screen_lock_portrait_baseline, screen_lock_rotation_baseline, security_update_good_baseline, signal_cellular_null_baseline, store_mall_directory_baseline, send_time_extension_baseline, send_time_extension_outlined, sentiment_satisfied_baseline, settings_brightness_baseline, settings_input_hdmi_baseline, shopping_cart_checkout_sharp, signal_cellular_alt_baseline, signal_cellular_off_baseline, sports_martial_arts_baseline, sports_martial_arts_outlined, send_time_extension_rounded, settings_bluetooth_baseline, share_arrival_time_baseline, sports_martial_arts_rounded, sports_motorsports_baseline, stacked_line_chart_baseline, sentiment_neutral_baseline, settings_ethernet_baseline, settings_overscan_baseline, signal_wifi_4_bar_baseline, signal_wifi_0_bar_baseline, sim_card_download_baseline, slow_motion_video_baseline, speaker_notes_off_baseline, sports_basketball_baseline, sports_gymnastics_baseline, sports_gymnastics_outlined, sports_volleyball_baseline, stacked_bar_chart_baseline, stop_screen_share_baseline, self_improvement_baseline, send_and_archive_baseline, send_time_extension_sharp, settings_display_baseline, settings_suggest_baseline, sports_gymnastics_rounded, sports_martial_arts_sharp, screen_rotation_baseline, security_update_baseline, settings_remote_baseline, shopping_basket_baseline, signal_wifi_bad_baseline, signal_wifi_off_baseline, social_distance_baseline, space_dashboard_baseline, sports_baseball_baseline, sports_football_baseline, sports_handball_baseline, strikethrough_s_baseline, safety_divider_baseline, send_to_mobile_baseline, settings_phone_baseline, settings_power_baseline, settings_voice_baseline, share_location_baseline, sim_card_alert_baseline, snippet_folder_baseline, sports_cricket_baseline, sports_esports_baseline, sports_gymnastics_sharp, sports_kabaddi_baseline, star_purple500_baseline, satellite_alt_baseline, satellite_alt_outlined, schedule_send_baseline, sd_card_alert_baseline, sensor_window_baseline, settings_cell_baseline, shopping_cart_baseline, shutter_speed_baseline, skateboarding_baseline, skip_previous_baseline, smart_display_baseline, smoking_rooms_baseline, sort_by_alpha_baseline, south_america_baseline, south_america_outlined, speaker_group_baseline, speaker_notes_baseline, speaker_phone_baseline, sports_hockey_baseline, sports_soccer_baseline, sports_tennis_baseline, sticky_note_2_baseline, satellite_alt_rounded, saved_search_baseline, scatter_plot_baseline, screen_share_baseline, scuba_diving_baseline, scuba_diving_outlined, shopping_bag_baseline, smart_button_baseline, smart_screen_baseline, snowboarding_baseline, soup_kitchen_baseline, soup_kitchen_outlined, south_america_rounded, sports_rugby_baseline, sports_score_baseline, star_outline_baseline, scuba_diving_rounded, sensor_door_baseline, sensors_off_baseline, shield_moon_baseline, shield_moon_outlined, snowshoeing_baseline, soup_kitchen_rounded, splitscreen_baseline, sports_golf_baseline, square_foot_baseline, star_border_baseline, stop_circle_baseline, satellite_alt_sharp, scoreboard_baseline, scoreboard_outlined, screenshot_baseline, sd_storage_baseline, search_off_baseline, select_all_baseline, shield_moon_rounded, short_text_baseline, show_chart_baseline, shuffle_on_baseline, single_bed_baseline, smartphone_baseline, smoke_free_baseline, sms_failed_baseline, snowmobile_baseline, south_america_sharp, south_east_baseline, south_west_baseline, spellcheck_baseline, sports_bar_baseline, sports_mma_baseline, ssid_chart_baseline, ssid_chart_outlined, storefront_baseline, straighten_baseline, streetview_baseline, sanitizer_baseline, satellite_baseline, scoreboard_rounded, scuba_diving_sharp, skip_next_baseline, slideshow_baseline, smart_toy_baseline, soup_kitchen_sharp, space_bar_baseline, ssid_chart_rounded, star_half_baseline, star_rate_baseline, save_alt_baseline, schedule_baseline, security_baseline, set_meal_baseline, settings_baseline, shield_moon_sharp, shop_two_baseline, shortcut_baseline, signpost_baseline, signpost_outlined, sim_card_baseline, sledding_baseline, snapchat_baseline, snapchat_outlined, straight_baseline, straight_outlined, stroller_baseline, sailing_baseline, save_as_baseline, save_as_outlined, savings_baseline, scanner_baseline, science_baseline, scoreboard_sharp, sd_card_baseline, segment_baseline, sensors_baseline, shopify_baseline, shopify_outlined, shuffle_baseline, signpost_rounded, snapchat_rounded, snowing_baseline, speaker_baseline, ssid_chart_sharp, stadium_baseline, stadium_outlined, storage_baseline, straight_rounded, subject_baseline, save_as_rounded, schema_baseline, school_baseline, search_baseline, shield_baseline, shop_2_baseline, shopify_rounded, shower_baseline, snooze_baseline, source_baseline, sports_baseline, square_baseline, square_outlined, stadium_rounded, stairs_baseline, stream_baseline, scale_baseline, scale_outlined, score_baseline, share_baseline, signpost_sharp, snapchat_sharp, south_baseline, speed_baseline, spoke_baseline, spoke_outlined, square_rounded, stars_baseline, start_baseline, start_outlined, store_baseline, storm_baseline, straight_sharp, style_baseline, save_as_sharp, save_baseline, scale_rounded, sell_baseline, send_baseline, shop_baseline, shopify_sharp, sick_baseline, soap_baseline, sort_baseline, spoke_rounded, stadium_sharp, star_baseline, start_rounded, stop_baseline, sip_baseline, sms_baseline, spa_baseline, square_sharp, scale_sharp, sd_baseline, spoke_sharp, start_sharp, radio_button_unchecked_baseline, remove_circle_outline_baseline, rotate_90_degrees_ccw_baseline, radio_button_checked_baseline, remove_shopping_cart_baseline, replay_circle_filled_baseline, report_gmailerrorred_baseline, rotate_90_degrees_cw_baseline, rotate_90_degrees_cw_outlined, rotate_90_degrees_cw_rounded, running_with_errors_baseline, restore_from_trash_baseline, real_estate_agent_baseline, record_voice_over_baseline, remove_from_queue_baseline, rotate_90_degrees_cw_sharp, radio_button_off_baseline, remove_moderator_baseline, room_preferences_baseline, roundabout_right_baseline, roundabout_right_outlined, radio_button_on_baseline, reduce_capacity_baseline, restaurant_menu_baseline, roundabout_left_baseline, roundabout_left_outlined, roundabout_right_rounded, remove_red_eye_baseline, report_problem_baseline, roller_skating_baseline, roller_skating_outlined, roundabout_left_rounded, rounded_corner_baseline, railway_alert_baseline, recent_actors_baseline, remove_circle_baseline, repeat_one_on_baseline, request_quote_baseline, rocket_launch_baseline, rocket_launch_outlined, roller_skating_rounded, roundabout_right_sharp, r_mobiledata_baseline, ramen_dining_baseline, receipt_long_baseline, request_page_baseline, restore_page_baseline, rocket_launch_rounded, room_service_baseline, rotate_right_baseline, roundabout_left_sharp, rate_review_baseline, remember_me_baseline, remove_done_baseline, restart_alt_baseline, ring_volume_baseline, roller_skating_sharp, rotate_left_baseline, rule_folder_baseline, ramp_right_baseline, ramp_right_outlined, repeat_one_baseline, report_off_baseline, restaurant_baseline, rocket_launch_sharp, run_circle_baseline, ramp_left_baseline, ramp_left_outlined, ramp_right_rounded, read_more_baseline, recommend_baseline, rectangle_baseline, rectangle_outlined, recycling_baseline, recycling_outlined, repeat_on_baseline, replay_10_baseline, replay_30_baseline, reply_all_baseline, rice_bowl_baseline, rv_hookup_baseline, ramp_left_rounded, rectangle_rounded, recycling_rounded, replay_5_baseline, reset_tv_baseline, rss_feed_baseline, ramp_right_sharp, raw_off_baseline, receipt_baseline, refresh_baseline, reorder_baseline, restore_baseline, reviews_baseline, roofing_baseline, ramp_left_sharp, raw_on_baseline, rectangle_sharp, recycling_sharp, reddit_baseline, reddit_outlined, redeem_baseline, remove_baseline, repeat_baseline, replay_baseline, report_baseline, rocket_baseline, rocket_outlined, router_baseline, rowing_baseline, radar_baseline, radio_baseline, reddit_rounded, reply_baseline, rocket_rounded, route_baseline, route_outlined, redo_baseline, room_baseline, route_rounded, rsvp_baseline, rule_baseline, reddit_sharp, rocket_sharp, rtt_baseline, route_sharp, update_disabled_baseline, u_turn_right_baseline, u_turn_right_outlined, u_turn_left_baseline, u_turn_left_outlined, u_turn_right_rounded, unfold_less_baseline, unfold_more_baseline, unpublished_baseline, unsubscribe_baseline, upload_file_baseline, u_turn_left_rounded, u_turn_right_sharp, unarchive_baseline, u_turn_left_sharp, umbrella_baseline, upcoming_baseline, upgrade_baseline, usb_off_baseline, update_baseline, upload_baseline, undo_baseline, usb_baseline, transfer_within_a_station_baseline, text_rotation_angledown_baseline, text_rotation_angleup_baseline, text_rotate_vertical_baseline, text_rotation_down_baseline, text_rotation_none_baseline, thumb_down_off_alt_baseline, transit_enterexit_baseline, turn_slight_right_baseline, turn_slight_right_outlined, table_restaurant_baseline, table_restaurant_outlined, thumb_up_off_alt_baseline, tips_and_updates_baseline, tips_and_updates_outlined, trending_neutral_baseline, turn_sharp_right_baseline, turn_sharp_right_outlined, turn_slight_left_baseline, turn_slight_left_outlined, turn_slight_right_rounded, table_restaurant_rounded, temple_buddhist_baseline, temple_buddhist_outlined, thermostat_auto_baseline, timer_10_select_baseline, tips_and_updates_rounded, turn_sharp_left_baseline, turn_sharp_left_outlined, turn_sharp_right_rounded, turn_slight_left_rounded, tab_unselected_baseline, tablet_android_baseline, takeout_dining_baseline, temple_buddhist_rounded, text_rotate_up_baseline, theater_comedy_baseline, thumb_down_alt_baseline, thumbs_up_down_baseline, timer_3_select_baseline, travel_explore_baseline, turn_sharp_left_rounded, turn_slight_right_sharp, table_restaurant_sharp, text_decrease_baseline, text_decrease_outlined, text_increase_baseline, text_increase_outlined, time_to_leave_baseline, tips_and_updates_sharp, track_changes_baseline, trending_down_baseline, trending_flat_baseline, turn_sharp_right_sharp, turn_slight_left_sharp, turned_in_not_baseline, tap_and_play_baseline, temple_buddhist_sharp, temple_hindu_baseline, temple_hindu_outlined, text_decrease_rounded, text_increase_rounded, text_snippet_baseline, thumb_up_alt_baseline, turn_sharp_left_sharp, table_chart_baseline, temple_hindu_rounded, text_fields_baseline, text_format_baseline, tire_repair_baseline, tire_repair_outlined, transgender_baseline, trending_up_baseline, trip_origin_baseline, two_wheeler_baseline, table_rows_baseline, table_view_baseline, tablet_mac_baseline, taxi_alert_baseline, text_decrease_sharp, text_increase_sharp, thermostat_baseline, thumb_down_baseline, tire_repair_rounded, toggle_off_baseline, turn_right_baseline, turn_right_outlined, table_bar_baseline, table_bar_outlined, tag_faces_baseline, temple_hindu_sharp, timelapse_baseline, timer_off_baseline, toggle_on_baseline, touch_app_baseline, transform_baseline, translate_baseline, turn_left_baseline, turn_left_outlined, turn_right_rounded, turned_in_baseline, table_bar_rounded, task_alt_baseline, telegram_baseline, telegram_outlined, terminal_baseline, terminal_outlined, theaters_baseline, thumb_up_baseline, timeline_baseline, timer_10_baseline, tire_repair_sharp, tonality_baseline, tungsten_baseline, turn_left_rounded, telegram_rounded, terminal_rounded, terrain_baseline, textsms_baseline, texture_baseline, timer_3_baseline, traffic_baseline, turn_right_sharp, table_bar_sharp, tablet_baseline, tiktok_baseline, tiktok_outlined, turn_left_sharp, tv_off_baseline, tapas_baseline, telegram_sharp, terminal_sharp, tiktok_rounded, timer_baseline, title_baseline, today_baseline, token_baseline, token_outlined, topic_baseline, train_baseline, task_baseline, token_rounded, toll_baseline, tour_baseline, toys_baseline, tram_baseline, tune_baseline, tab_baseline, tag_baseline, tiktok_sharp, toc_baseline, try_baseline, tty_baseline, token_sharp, tv_baseline, system_security_update_warning_baseline, system_security_update_good_baseline, switch_access_shortcut_add_baseline, switch_access_shortcut_add_outlined, switch_access_shortcut_add_rounded, switch_access_shortcut_add_sharp, supervised_user_circle_baseline, swap_horizontal_circle_baseline, switch_access_shortcut_baseline, switch_access_shortcut_outlined, system_security_update_baseline, switch_access_shortcut_rounded, swap_vertical_circle_baseline, switch_access_shortcut_sharp, supervisor_account_baseline, system_update_alt_baseline, swap_vert_circle_baseline, system_update_tv_baseline, swipe_right_alt_baseline, swipe_right_alt_outlined, surround_sound_baseline, swipe_down_alt_baseline, swipe_down_alt_outlined, swipe_left_alt_baseline, swipe_left_alt_outlined, swipe_right_alt_rounded, swipe_vertical_baseline, swipe_vertical_outlined, switch_account_baseline, subscriptions_baseline, subtitles_off_baseline, sunny_snowing_baseline, support_agent_baseline, swipe_down_alt_rounded, swipe_left_alt_rounded, swipe_vertical_rounded, switch_camera_baseline, sync_disabled_baseline, system_update_baseline, swipe_right_alt_sharp, swipe_up_alt_baseline, swipe_up_alt_outlined, switch_right_baseline, switch_video_baseline, sync_problem_baseline, superscript_baseline, swipe_down_alt_sharp, swipe_left_alt_sharp, swipe_right_baseline, swipe_right_outlined, swipe_up_alt_rounded, swipe_vertical_sharp, switch_left_baseline, swap_calls_baseline, swap_horiz_baseline, swipe_down_baseline, swipe_down_outlined, swipe_left_baseline, swipe_left_outlined, swipe_right_rounded, subscript_baseline, subtitles_baseline, summarize_baseline, swap_vert_baseline, swipe_down_rounded, swipe_left_rounded, swipe_up_alt_sharp, synagogue_baseline, synagogue_outlined, sync_lock_baseline, sync_lock_outlined, swipe_right_sharp, swipe_up_baseline, swipe_up_outlined, synagogue_rounded, sync_alt_baseline, sync_lock_rounded, support_baseline, surfing_baseline, swipe_down_sharp, swipe_left_sharp, swipe_up_rounded, subway_baseline, synagogue_sharp, sync_lock_sharp, sunny_baseline, swipe_baseline, swipe_up_sharp, sync_baseline, youtube_searched_for_baseline, yard_baseline, wifi_tethering_error_rounded_baseline, wifi_protected_setup_baseline, wifi_tethering_error_baseline, wifi_tethering_error_outlined, wifi_tethering_off_baseline, workspaces_outline_baseline, wallet_membership_baseline, wheelchair_pickup_baseline, wifi_tethering_error_sharp, workspace_premium_baseline, workspace_premium_outlined, workspaces_filled_baseline, workspace_premium_rounded, wallet_giftcard_baseline, waterfall_chart_baseline, wb_incandescent_baseline, wifi_calling_3_baseline, wifi_tethering_baseline, workspace_premium_sharp, wrong_location_baseline, wallet_travel_baseline, warning_amber_baseline, wb_iridescent_baseline, wb_twighlight_baseline, web_asset_off_baseline, where_to_vote_baseline, wifi_password_baseline, wifi_password_outlined, water_damage_baseline, wifi_calling_baseline, wifi_channel_baseline, wifi_channel_outlined, wifi_password_rounded, woo_commerce_baseline, woo_commerce_outlined, work_outline_baseline, watch_later_baseline, waving_hand_baseline, waving_hand_outlined, wb_twilight_baseline, web_stories_baseline, wifi_channel_rounded, woo_commerce_rounded, water_drop_baseline, water_drop_outlined, waving_hand_rounded, wifi_password_sharp, workspaces_baseline, wallpaper_baseline, warehouse_baseline, warehouse_outlined, watch_off_baseline, watch_off_outlined, water_drop_rounded, wb_cloudy_baseline, web_asset_baseline, wifi_channel_sharp, wifi_find_baseline, wifi_find_outlined, wifi_lock_baseline, woo_commerce_sharp, wordpress_baseline, wordpress_outlined, wrap_text_baseline, warehouse_rounded, watch_off_rounded, waving_hand_sharp, wb_shade_baseline, wb_sunny_baseline, whatsapp_baseline, whatsapp_outlined, whatshot_baseline, wifi_find_rounded, wifi_off_baseline, wine_bar_baseline, wordpress_rounded, work_off_baseline, warning_baseline, water_drop_sharp, wb_auto_baseline, webhook_baseline, webhook_outlined, weekend_baseline, whatsapp_rounded, widgets_baseline, wysiwyg_baseline, warehouse_sharp, watch_off_sharp, webhook_rounded, wechat_baseline, wechat_outlined, wifi_find_sharp, window_baseline, wordpress_sharp, watch_baseline, water_baseline, waves_baseline, wechat_rounded, whatsapp_sharp, woman_baseline, woman_outlined, wash_baseline, webhook_sharp, west_baseline, wifi_baseline, woman_rounded, work_baseline, web_baseline, wechat_sharp, wc_baseline, woman_sharp, vertical_align_bottom_baseline, vertical_align_center_baseline, vertical_distribute_baseline, videogame_asset_off_baseline, vertical_align_top_baseline, video_camera_front_baseline, volunteer_activism_baseline, video_camera_back_baseline, video_collection_baseline, view_comfortable_baseline, view_compact_alt_baseline, view_compact_alt_outlined, videogame_asset_baseline, view_compact_alt_rounded, volume_down_alt_baseline, vertical_split_baseline, video_settings_baseline, view_comfy_alt_baseline, view_comfy_alt_outlined, visibility_off_baseline, voice_over_off_baseline, verified_user_baseline, video_library_baseline, view_carousel_baseline, view_comfy_alt_rounded, view_compact_alt_sharp, view_headline_baseline, view_timeline_baseline, view_timeline_outlined, vaping_rooms_baseline, vaping_rooms_outlined, video_stable_baseline, videocam_off_baseline, view_compact_baseline, view_sidebar_baseline, view_timeline_rounded, vaping_rooms_rounded, video_label_baseline, view_agenda_baseline, view_column_baseline, view_comfy_alt_sharp, view_kanban_baseline, view_kanban_outlined, view_module_baseline, view_stream_baseline, volume_down_baseline, volume_mute_baseline, vpn_key_off_baseline, vpn_key_off_outlined, video_call_baseline, video_file_baseline, video_file_outlined, view_array_baseline, view_comfy_baseline, view_in_ar_baseline, view_kanban_rounded, view_quilt_baseline, view_timeline_sharp, visibility_baseline, voice_chat_baseline, volume_off_baseline, vpn_key_off_rounded, vape_free_baseline, vape_free_outlined, vaping_rooms_sharp, vibration_baseline, video_file_rounded, view_cozy_baseline, view_cozy_outlined, view_list_baseline, view_week_baseline, voicemail_baseline, volume_up_baseline, vaccines_baseline, vaccines_outlined, vape_free_rounded, verified_baseline, videocam_baseline, view_cozy_rounded, view_day_baseline, view_kanban_sharp, vignette_baseline, vpn_key_off_sharp, vpn_lock_baseline, vaccines_rounded, video_file_sharp, vpn_key_baseline, vape_free_sharp, view_cozy_sharp, vrpano_baseline, vaccines_sharp, villa_baseline, zoom_out_map_baseline, zoom_in_map_baseline, zoom_in_map_outlined, zoom_in_map_rounded, zoom_in_map_sharp, zoom_out_baseline, zoom_in_baseline}
❌ new codepoints file does not contain all 7315 existing codepoints. Missing: {baby_changing_station, battery_charging_full, browser_not_supported, bluetooth_connected, bluetooth_searching, bluetooth_disabled, branding_watermark, border_horizontal, brightness_medium, batch_prediction, bookmark_outline, breakfast_dining, battery_unknown, bluetooth_audio, bluetooth_drive, bookmark_border, bookmark_remove, border_vertical, brightness_auto, brightness_high, business_center, bedroom_parent, bookmark_added, brightness_low, bakery_dining, battery_alert, battery_saver, bedroom_child, block_flipped, blur_circular, border_bottom, brunch_dining, backup_table, battery_full, beach_access, bedroom_baby, bike_scooter, bookmark_add, border_clear, border_color, border_inner, border_outer, border_right, border_style, brightness_5, brightness_4, brightness_1, brightness_7, brightness_6, brightness_3, brightness_2, broken_image, bubble_chart, build_circle, battery_std, blur_linear, book_online, border_left, border_all, border_top, bug_report, burst_mode, backspace, bar_chart, bloodtype, bluetooth, bookmarks, bus_alert, backpack, bathroom, beenhere, blur_off, bookmark, bungalow, business, balcony, bathtub, bedtime, biotech, blender, blur_on, backup, ballot, badge, bento, block, brush, build, bolt, book, bed, airline_seat_individual_suite, airline_seat_legroom_reduced, airline_seat_legroom_normal, airline_seat_recline_normal, airline_seat_legroom_extra, airline_seat_recline_extra, airline_seat_flat_angled, align_horizontal_center, account_balance_wallet, align_horizontal_right, arrow_drop_down_circle, airplanemode_inactive, align_horizontal_left, align_vertical_bottom, align_vertical_center, admin_panel_settings, assignment_turned_in, assistant_navigation, add_photo_alterna…

---
## [ModruKinstealer/CS50ProblemSets](https://github.com/ModruKinstealer/CS50ProblemSets)@[51677d18bf...](https://github.com/ModruKinstealer/CS50ProblemSets/commit/51677d18bfa8324b5b1056af9df90c6bc92d682d)
#### Thursday 2022-03-10 04:25:31 by ModruKinstealer

Problem set3: tideman

Specification
https://cs50.harvard.edu/x/2022/psets/3/tideman/

You should not modify anything else in tideman.c other than the implementations of the vote, record_preferences, add_pairs, sort_pairs, lock_pairs, and print_winner functions (and the inclusion of additional header files, if you’d like). You are permitted to add additional functions to tideman.c, so long as you do not change the declarations of any of the existing functions.

I did fairly well on this pset, up until sort_pairs. I struggled with getting it to work properly but managed to figure it out. lock_pairs I spent over a week on and probably in the 30-40 hours? I'm not sure how much I should have actually spent, I spent a long time working on it before I realized that my recursive call to cycle_created had the arguments reversed and I was sending (loser, winner) instead of (winner, loser) It still took me another few hours to get everything nailed down in that one. In the end I'm not sure that I actually learned anything from trying to implement the recursive function of cycle_created.  If I get time I might come back to tideman after the course and see if I can solve it more easily/faster. I did find numerous posts about how tideman was the hardest problem in the entire course and that a lot of people struggle with it so I'm not totally upset with it taking so long. I'm glad to have completed it with minimal looks at hints beyond something like https://gist.github.com/nicknapoli82/6c5a1706489e70342e9a0a635ae738c9
My biggest frustration came from the feeling that at this point I don't think I could have come close to figuring out this program from scratch if I was tasked to do so in the real world. I would definitely need assistance from a senior dev or something. I feel like I understand the tideman process itself, but translating it to code was very difficult.
There were a couple other functions that I thought would have been good candidates for a recursive function but I decided against it, one because it specifcally stated the function should only be called once and also because we couldn't change the functions and they were void for both arguments and returns. I figured if I created a custom function that did the function recursively and the original one basically just called the custom function it wasn't really following the specifications of the problem set. 

Print_winner I spent way more time on that I should have had to. I had implemented it references pairs[], my thinking was that we did all the work to create and sort pairs and cycling through that would take a lot less cycles than cycling through locked[][]. However the function just would not pass check50 using pairs and I found a mention on the cs50 discord that check50 wouldn't pass it if you used pairs over locked so I re-did the code to use locked[][] and it worked within minutes.

Last note, I'm getting pretty good at the implemented style guide for cs50. I did have a few changes I had to make where I missed a space, if( instead of if (, or variable+1 instead of variable + 1. But less than a dozen missed spaces in 284 lines of codes seems relatively reasonable at this stage so I'm happy with my progress there.

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[eeb5465931...](https://github.com/Tastyfish/-tg-station/commit/eeb546593148ce940e9adac2c663c453d6557247)
#### Thursday 2022-03-10 05:24:57 by vincentiusvin

Ordnance Content Update: Scientific Papers (#62284)

How do I play/test/operate this?

Download NT Frontier on any modular computers. It should debrief you on what experiments are available and how to publish.
If you want to do a bomb experiment, make sure it's captured by the doppler array (as usual) and then print the experiments into a disk and publish it.
If you want to do a gas experiment, make the gas and either pump it into a tank and 1) overpressurize it with a "clear" gas like N2 or 2) overpressurize tanks with the gas itself. Make sure you do the overpressurizing in the compressor machine. When tanks are destroyed/ejected leaked gas will get recorded. Print it into a disk and publish it.
For publication, the file needs to be directly present inside the computer's HDD. This means you need to copy it first with the file manager.
Fill the data (if desired, it will autofill with boiler plate if you dont) and send away!
Doing experiments unlock nodes, while doing them well unlocks boosts (which are discounts but slightly more restrictive) which are purchaseable with NT Frontier.
If you are testing this and have access to admin tools, there are various premade bombs under obj/effect/spawner/newbomb

A doc I wrote detailing the why and what part of this PR.
https://hackmd.io/JOakSYVMSh2zU2YL5ju_-Q

---

# Intro

## The Problem(s)

Ordnance, (previously toxins) seems to lack a lot of content and things to do. The gameplay loop consists of making a bomb and then sending it off for credits or using it to refine cores. Ordnance at it's inception originally relies on players experimenting and finding the perfect mix over multiple rounds, but once the recipe for a "do-everything" mix got out, the original charm of individual discoveries becomes meaningless.

Another issue with ordnance is the odd difficulty curve. As a new player, ordnance is almost impossible to decipher, but once you watch a tutorial or read a wiki and can mail a 50k into space, there pretty much isn't anything else to do. Most players will be satisfied at this point without the gameplay loop encouraging them to understand or play more. The only thing you can do afterwards is to sink your teeth in and understand why that particular mix explodes the way it does. This again has a significant difficulty curve, but if you do that, the department doesn't acknowledge or reward that in any way. There are pretty much two huge spikes, with the latter one not really existing inside the department.

TLDR:
* The content being same-y over rounds.
* Odd difficulty curve: 
    1. A new player is oblivious to everything. 
    2. Those in the middle can repeat the final goal consistently without needing to understanding why
    3. There is nothing to justify spending more time in the department after reaching the midgame.

## Abstract

Scientific Papers aim to add a framework to run multiple experiments in ordnance. Adding more experiments scattered across various atmospheric aspects might allow players of various knowledge levels to still have something engaging to do. A new player should have an easier challange than to mail a 50K. While those that already can make bombs should have an easier time understanding why their bombs explode the way it does. Once they fully understand why, they can set their sights on taking advantage of another reaction to set their bomb off or hone one particular reaction down.

## Goals

* Have some intro-level challanges for new players.
* Have some semblance of late-game challanges for more experienced players.
* Explain the mechanics better for those in the middle of the road.
* Incentivize trying new things out in the department.
* Better integrate Ordnance with Experisci

## Boundaries / Dont's

* Do not incentivize people to learn ordnance by using PvP loots.
* Do not shake or change the reaction system by a huge amount.
* Disincentivize having a single god-mix that does everything.
****

# Main design pillars

## A. Framework surrounding the experiments

### A.1. New experiments

Add new experiments to the ExperiSci module. These will come in two flavours: New explosions to do, and various gas synthesis experiments. Both of these are actually supported by the map layout of ordnance right now, but there is no reason to do anything outside of making a 50k as fast as possible.

### A.2. Rewards for experiments: Cash and Techweb Boosts.

Scientific papers will add a separate experiment handling system. A single experiment will be graded into various tiers, each tier corresponding to the explosion size or amount of gas made.  Doing any tier of a specific experiment will unlock the discount for that specific reactions. A single explosion **WILL NOT** do multiple experiments (or even tiers) at once.

On publication, a partner can be selected. A single partner only has a specific criteria of experiments they want. The experiments will then be graded on "how good they are done", with the criteria being more punishing as tier increases. Publication will then reward scientific cooperation with the partnered partner. Players can spend this cooperation on techweb boosts. Techweb boosts are meant to be subservient to discount from experiments and will not shave a node's price to be lower than 500 points.

**Experiments will only unlock nodes, discounts are handled through this boost system.**
This is more for maintainability than anything.

### A.3. On Tedium

*This is a note on implementation more than anything, but I think this helps explains why several things are done.*

Due to the nature of atmospheric reactions in the game (they're all linear), tedium is a very important thing to consider. An experiment should have a sweet spot to aim for, but there should not be a point where further mastery is stopped dead on it's track with a reward cap.

Scientific Papers attempts to discourage this behaviour by having the "maximum score" scale off to infinity but with the rewards being smaller and smaller. The sweet spot is always there to aim for and should be well communicated with players, but on their last submission of an experiment topic players should be encouraged to do their best. There should always be a reward for pushing the system to it's limit as long as it doesn't completely nullify the other subdepartments. This is the reason why there is a hard limit on the number of publications and why the score calculation is a bit more complex than it needed to be.

## B. Gas Synthesis (Early-Mid Game)

Scientific papers will add one new machine that requests a tank to release x amounts of y gas. This will be accomplished by adding a tank pumping machine which will either burst or explode a tank, releasing the gas inside. The gas currently requested are BZ, Nitryl, Halon and Nob.

The overarching goal of this compressor machine is to present a gas synthesis challange for the players and to get them more accustomed to how a tank explodes. The gas synthesis part can always be changed in order to reflect the current state of atmospheric reactions.

## C. Explosion Changes (Mid-Late Game)

### C.1 Cause and effect.

The main theme of the explosion changes is establishing cause and effect of explosions. Reactions that happens inside a tank that's going to explode will be recorded and forwarded to a doppler array. Some experiments will require only a single cause to be present (think of it as isolating a variable). This is currently implemented for nobliumformation and pressure based bombs. Having other reactions occuring besides noblium formation will fail the first one, while having any reactions at all will fail the second one. 

Adding more explosions here will be a slight challange because as of now the game has only two reactions that can reliably make an explosion.

### C.2 Tools upgrade.

Doppler array has now been retrofitted to state the probable cause of an explosion, be it reactions or just overpressurization on gas merging. These should help intermediate players figure out what is causing an explosion.

Added a new functionality to the implosion compressor:
Basically performs the gas merging and reaction that TTV does in a machine and reports the results back as if someone uses an analyzer on them. Here to give players feedback so they can try and understand what is actually going on in a bomb.

## D. Player Interaction

There should be more room for more than 1 player to play ordnance simultaneously. Previously players are also able to split tasks, but this rarely happens because tritium synthesis needs only the gas chamber to be reconfigured. Now, different players can pick different experiments and work on them. Players can also do joint tasks on one single experiment. Gases like noblium will need tritium production and also a cooling module online.

Ordnance can also coordinate with their parent department on what they really need, be it money or research bonuses.

# Potential Changes

The best-case changes that can be implemented if the current roster of content isn't enough is more reactions that can be used in bombs. Eliminating bombs entirely goes against the spirit of the subdepartment, while adding new ones will need a lot of care and consideration.

Another possible change is to implement a "gas payload" bomb. Bombs that has a set number of unreacting gas inside that will increase the heat capacity, reduce the payload, and neccesitates more bespoke mixes.

Adding more gas synthesis experiments is discouraged. The main focus of ordnance should be bombs, with gas synthesis being a side project for ordnance. These are present to ease the introduction to bombs and provide some side content. 
There should be a somewhat well-justified goal in adding new synthesis experiments: e.g. BZ is there as a "tutorial" gas, Nitryl to introduce players to cooling/heating mixes, Halon to a more efficient tritium production, and Nob as a nudge to nobformation bombs and mastery over other aspects.

# Conclusion / Summary

Add more experiments to ordnance that players can take, accomplish this by:
1. Making the players perform gas synthesis or make bombs.
2. Have them collect the data, see if it fits the criteria. Explain why if it fits and why if it doesn't.
3. Have the player publish a paper.

Reward them based on how well did they do, give players agency both on the experiment phase and also publication phase.


---
TLDR: Added new experiment to toxins, added the framework for those experiments existing. Experiments comes in gas synthesis and also bombs but with more parameters. Experiments needs to be published through papers, various choices to be made there.

Implementation notes:

Because of how paper works, ordnance experiments are handled outside of experiment_handler components. My reasoning for this is twofold:

The experiments will be completed manually on publication and if the experiment isn't unlocked yet it will still be completed.
Experiment handler datums have several procs which require an atom-level parent, and I figured this is the most sensible and cleanest way to implement this without changing the experiment handler datum too much.

Small change to /obj/machinery/proc/power_change() signal ordering to adjust the state first and then send the signal. Didn't found any other usage of this signal except mine but barge down my door if it broke something.

Rewrote the ttv merge_gases() code to be slightly more readable.
A small code improvement for thermomachine to use tofixed (my fault).

Ordnance have been updated to enable the publication of papers
Several new explosive and gas synthesis experiments have been added to ordnance
Anomaly compressor has been TGUIzed and now supports simulating the reaction of the gases inside the ttv.
New tank compressor machine for toxins. You can overpressurize tanks with exotic gases and complete experiments.
Several techweb nodes are locked and require toxin experiments to complete.
Toxins can purchase boosts for various techweb nodes.
You no longer need to anchor doppler arrays for it to work.
Doppler array and implosion compressor now supports deconstruction, implosion compressor construction added.
Doppler now emits a red light to denote it's direction and it being on. Doppler not malf.
Implosion compressor renamed to anomaly refinery.
Created a new program tab "Science" for the downloader app. Removed Robotics.
Reworked the code for bombspawner (used in the cuban pete arcade game)

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[f4f0e04330...](https://github.com/clamor-s/u-boot/commit/f4f0e0433043f3643e416ebbf72452896ee7481d)
#### Thursday 2022-03-10 06:45:25 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[da3387e685...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/da3387e6857d91ece724e52c17ab0ef8b98172a6)
#### Thursday 2022-03-10 08:24:35 by Raja Kunal Pandit

Create 	750A - New Year and Hurry.cpp

Output Status: 

By Rajakunalpandit, contest: Good Bye 2016, problem: (A) New Year and Hurry, Accepted

Limak is going to participate in a contest on the last day of the 2016. The contest will start at 20:00 and will last four hours, exactly until midnight. There will be n problems, sorted by difficulty, i.e. problem 1 is the easiest and problem n is the hardest. Limak knows it will take him 5·i minutes to solve the i-th problem.

Limak's friends organize a New Year's Eve party and Limak wants to be there at midnight or earlier. He needs k minutes to get there from his house, where he will participate in the contest first.

How many problems can Limak solve if he wants to make it to the party?

Input
The only line of the input contains two integers n and k (1 ≤ n ≤ 10, 1 ≤ k ≤ 240) — the number of the problems in the contest and the number of minutes Limak needs to get to the party from his house.

Output
Print one integer, denoting the maximum possible number of problems Limak can solve so that he could get to the party at midnight or earlier.

Examples
inputCopy
3 222
outputCopy
2
inputCopy
4 190
outputCopy
4
inputCopy
7 1
outputCopy
7
Note
In the first sample, there are 3 problems and Limak needs 222 minutes to get to the party. The three problems require 5, 10 and 15 minutes respectively. Limak can spend 5 + 10 = 15 minutes to solve first two problems. Then, at 20:15 he can leave his house to get to the party at 23:57 (after 222 minutes). In this scenario Limak would solve 2 problems. He doesn't have enough time to solve 3 problems so the answer is 2.

In the second sample, Limak can solve all 4 problems in 5 + 10 + 15 + 20 = 50 minutes. At 20:50 he will leave the house and go to the party. He will get there exactly at midnight.

In the third sample, Limak needs only 1 minute to get to the party. He has enough time to solve all 7 problems.

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[7720f9f95a...](https://github.com/MrMelbert/tgstation/commit/7720f9f95ab56b21b84cb56b4e8f1af09b566470)
#### Thursday 2022-03-10 08:34:19 by MrMelbert

god damn devil removal
- this check was removed when devil was and i think it's kinda important to prevent stacking lichdom

---
## [aospa-sdm660/android_kernel_asus_sdm660](https://github.com/aospa-sdm660/android_kernel_asus_sdm660)@[e60f6dfbdd...](https://github.com/aospa-sdm660/android_kernel_asus_sdm660/commit/e60f6dfbdde59a8eb38b4df176817152bfab9968)
#### Thursday 2022-03-10 09:00:29 by Masahiro Yamada

kbuild: use more portable 'command -v' for cc-cross-prefix

To print the pathname that will be used by shell in the current
environment, 'command -v' is a standardized way. [1]

'which' is also often used in scripts, but it is less portable.

When I worked on commit bd55f96 ("kbuild: refactor cc-cross-prefix
implementation"), I was eager to use 'command -v' but it did not work.
(The reason is explained below.)

I kept 'which' as before but got rid of '> /dev/null 2>&1' as I
thought it was no longer needed. Sorry, I was wrong.

It works well on my Ubuntu machine, but Alexey Brodkin reports noisy
warnings on CentOS7 when 'which' fails to find the given command in
the PATH environment.

  $ which foo
  which: no foo in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin)

Given that behavior of 'which' depends on system (and it may not be
installed by default), I want to try 'command -v' once again.

The specification [1] clearly describes the behavior of 'command -v'
when the given command is not found:

  Otherwise, no output shall be written and the exit status shall reflect
  that the name was not found.

However, we need a little magic to use 'command -v' from Make.

$(shell ...) passes the argument to a subshell for execution, and
returns the standard output of the command.

Here is a trick. GNU Make may optimize this by executing the command
directly instead of forking a subshell, if no shell special characters
are found in the command and omitting the subshell will not change the
behavior.

In this case, no shell special character is used. So, Make will try
to run it directly. However, 'command' is a shell-builtin command,
then Make would fail to find it in the PATH environment:

  $ make ARCH=m68k defconfig
  make: command: Command not found
  make: command: Command not found
  make: command: Command not found

In fact, Make has a table of shell-builtin commands because it must
ask the shell to execute them.

Until recently, 'command' was missing in the table.

This issue was fixed by the following commit:

| commit 1af314465e5dfe3e8baa839a32a72e83c04f26ef
| Author: Paul Smith <psmith@gnu.org>
| Date:   Sun Nov 12 18:10:28 2017 -0500
|
|     * job.c: Add "command" as a known shell built-in.
|
|     This is not a POSIX shell built-in but it's common in UNIX shells.
|     Reported by Nick Bowler <nbowler@draconx.ca>.

Because the latest release is GNU Make 4.2.1 in 2016, this commit is
not included in any released versions. (But some distributions may
have back-ported it.)

We need to trick Make to spawn a subshell. There are various ways to
do so:

 1) Use a shell special character '~' as dummy

    $(shell : ~; command -v $(c)gcc)

 2) Use a variable reference that always expands to the empty string
    (suggested by David Laight)

    $(shell command$${x:+} -v $(c)gcc)

 3) Use redirect

    $(shell command -v $(c)gcc 2>/dev/null)

I chose 3) to not confuse people. The stderr would not be polluted
anyway, but it will provide extra safety, and is easy to understand.

Tested on Make 3.81, 3.82, 4.0, 4.1, 4.2, 4.2.1

[1] http://pubs.opengroup.org/onlinepubs/9699919799/utilities/command.html

Fixes: bd55f96 ("kbuild: refactor cc-cross-prefix implementation")
Cc: linux-stable <stable@vger.kernel.org> # 5.1
Reported-by: Alexey Brodkin <abrodkin@synopsys.com>
Tested-by: Alexey Brodkin <abrodkin@synopsys.com>
Change-Id: I763dc6a4b8cd43a6ed820219f99d9256ab44308a
Signed-off-by: Kunmun <kunmun.devroms@gmail.com>

---
## [bhalevy/scylla](https://github.com/bhalevy/scylla)@[674d3a5a84...](https://github.com/bhalevy/scylla/commit/674d3a5a8465c365cb0e608f4c921e3c12b758c6)
#### Thursday 2022-03-10 09:37:28 by Nadav Har'El

compound_compat.hh: add missing methods of iterator

While debugging legacy_compound_view, I noticed that it cannot be used
as a C++20 std::ranges::input_range because it is missing some trivial
methods. So let's fix this, and make the life of future developers a
little bit easier.

The two trivial methods we need to implement:

1. A postfix increment operator. We already had a prefix increment
   operator, but the C++20 concept weakly_iterable also needs postfix.

2. By mistake (this will be corrected in https://wg21.link/P2325R3),
   weakly_iterable also required the default_initialized concept, so
   our iterator type also needs a default constructor.
   We'll never actually use this silly constructor, and when this C++20
   standard mistake is corrected, we can remove this constructor.

After this patch, a legacy_compound_view is accepted for the C++20
ranges::input_range concept.

Signed-off-by: Nadav Har'El <nyh@scylladb.com>

---
## [dandelion64-Repos/android_kernel_xiaomi_dandelion](https://github.com/dandelion64-Repos/android_kernel_xiaomi_dandelion)@[cf9f829523...](https://github.com/dandelion64-Repos/android_kernel_xiaomi_dandelion/commit/cf9f829523c09272ddddad7decc0e4f15b4976bb)
#### Thursday 2022-03-10 10:14:43 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.9
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.9 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. exclude kill() changes to avoid struct kernel_siginfo usage
 4. exclude copy_siginfo_from_user_any() to avoid struct kernel_siginfo usage
 5. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 6. replaced COND_SYSCALL with cond_syscall
 7. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 8. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I00f1c618b2e9dbafae4d4113ad4d8a1a44b6957c
Signed-off-by: Suren Baghdasaryan <surenb@google.com>

---
## [mh-cz/GameMaker-Foreach](https://github.com/mh-cz/GameMaker-Foreach)@[217dfbb442...](https://github.com/mh-cz/GameMaker-Foreach/commit/217dfbb442f9e9094832752267de389c24eb530a)
#### Thursday 2022-03-10 11:46:21 by Matěj Hula

Fixed returning "undefined"...

...when looping through something with no data. It returns nothing now. Such a stupid bug and it took me 3 months to realize it holy fuck..

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[baf01aedce...](https://github.com/mrakgr/The-Spiral-Language/commit/baf01aedcef4e95ec039a2bd1d481a1ae7ead238)
#### Thursday 2022-03-10 11:54:01 by Marko Grdinić

"9:50am. I am up. Let me chill just a bit and then I will start. I am going to watch those short procedural texturing vids on the top of Youtube and then dive into the 5h course.

10:15am. https://youtu.be/9ngbOV0YKbk?t=240
Advanced Procedural Texturing

Let me resume this from yesterday. This is using some program I've never heard about called Clarisse.

https://youtu.be/j-B5Cib_DXw
Displace Geometry in Houdini || Quick Tricks

Let me watch this first, I actually don't know how to apply displacement on geometry directly.

https://youtu.be/j-B5Cib_DXw?t=34

Ah, displace is actually in a VOP.

10:30am. Let me go back that other tutorial. I've played with displacement a bit.

https://youtu.be/oCQhnVl-xrI
What is Clarisse?

10:35am. https://youtu.be/9ngbOV0YKbk?t=424

I've been playing around with UV noise in the V-Ray shader nodes, but it never worked for me for some reason.

https://www.reddit.com/r/vfx/comments/lsxu3n/what_is_clarisse_used_for/
> Yeah as already mentioned, it can handle a huge amount of polys and have them viewable in the viewport instead of bounding boxes. I am talking billions. Its definitely suited towards environments.

> I would say if your really technical and perhaps know some Houdini then continue down that path. But its really good for people coming from a more DMP and creative background. Its quite easy to get scattering and make environments quickly. I think you can get creating stuff quicker than you would if learning Houdini from scratch.

> I actually made a timelapse the other day of a project I made using it, will give you some idea of it: https://www.youtube.com/watch?v=Fo7pOE5_2EU

> You can see by the end that the scene had 480 million polys in it just fine.

This is interesting.

> "Crashisse" - wish we had thought of that. It was painful. Open a scene, wait 40 minutes to load, make a few changes, crash, repeat. In a normal working day, we got about an hour or two worth of work done.

What the hell? Apparently this was an issue in old versions.

> I absolutely love clarisse for env work and there is nothing like it out there where you can make changes and experiment like you can in clarisse. Houdini is an amazing software that I love and use daily but it is not a clarisse alternative. Houdini can't display 1/1000000th the geometry you can display and move around in clarisse so you are looking at proxies of proxies while working on big env's as opposed to being able to like "hey let me move around this 6 million poly tree in realtime in render view while it's rendering to find the best composition" like you can in Clarisse.

10:50am. https://youtu.be/9ngbOV0YKbk?t=840

I can't really follow this, but it does not matter.

10:55am. https://youtu.be/9ngbOV0YKbk?t=1038

I saw this in Blender. What is a point cloud texture?

Ohhh, this is what I had in mind for doing the water around the pool. I should look up point clouds in Houdini.

https://youtu.be/RfaBNoicXp4
Find Points on Geometry with Point Clouds | Houdini VEX Quickies

Let me do a bit of research in this. This might be an alternative to painting masks. Instead painting masks, I could drop down points and transfer attribute. That would allow the system to be persistent to the changes in the underlying geometry. It actually has a lot of advantages compared to mask painting.

https://youtu.be/uTPR0cUVRdg
Magic Market | Procedural Rocks 4 | Procedural Texturing

I'll skip the Blender tutorials as my focus on is on Houdini. Let me watch this for a bit. After that I'll dive into the 5h tutorial from the start.

https://www.sidefx.com/tutorials/magic-market-procedural-rocks/

I'll leave this for later if at all. Let me just go with the Rebelway tutorial. I do not need so many rock tutorials.

11:15am. https://docs.chaos.com/display/VMAX/VRayDistanceTex

I just remembered I saw the distance texture. Maybe this is what I need for those water puddles around the pool.

Also I just realized - in the material palette I have the assets from the V-Ray library. This will make using them a lot easier.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Distance

This could be really useful for water. I can just place a bunch of points and pass this as the point cloud. Brilliant. This resolves one of my issues.

I just remembered that Houdini has the Spray Paint node. I could use that to spray a path.

11:25am. This is wonderful. If you deform the geometry in the earlier nodes the sprayed points get projected onto its surface. It has a lot of roboustness. It seems the projection takes into account the original orientation of the points rather than just placing them on the nearest point. Nice. Though it might be better if it projected the stoke itself rather than the points. It does not matter right now.

I am satisfied. Let me go back to the master class.

12pm. https://youtu.be/kz-_z3wREbY?t=1658

Let me skip this pipeline stuff. It is not something I need to be concerned about. Let me go back where I was yesterday.

https://youtu.be/kz-_z3wREbY?t=10611

Oh, this thing he does to put in regions is brilliant. Why did I never think of this? I should keep it in mind.

12:40pm. https://youtu.be/kz-_z3wREbY?t=11524

Let me stop here in the middle of part 2.

This is good enough.

Let me do the chores and have breakfast here and I am going to try going with the mask painting plan. It should work well for the leaf.

I've got this thing in the bag. It won't give me trouble for much longer. I can do an enormous amount without ever touching UV unwrapping by hand. And if I use UV projections not even textures themselves will give me particular trouble.

I can just tream them as a different kind of noise. For specific things there will always be masks and geometry.

I am thinking back to that banana tutorial, and with the understanding I have now I'd have no trouble dealing with it without having to go into an app like 3d coat.

12:50pm. Let me do the chores."

---
## [VTPDevelopment/Silk](https://github.com/VTPDevelopment/Silk)@[a52188a680...](https://github.com/VTPDevelopment/Silk/commit/a52188a680b985e9d8bf17e86059d0d54d8d9ff0)
#### Thursday 2022-03-10 12:39:17 by Velvet

🐛 FINALLY FIX CACHING ODDITIES

THIS HAS PLAGUED ME FOR MONTHS AND I FINALLY FIGURED IT OUT

SLIDING EXPIRATIONS SUCK. DO NOT USE THEM.
 Well, they suck when you expect absolute expirations to do anything.
I tried for months to fix this on various occasions, and I was ready to pull out Redis until I finally figured out that sliding expirations are the absolute devil :)

Absolute expiration means NOTHING if you're using a sliding expiration. Though it if we set the absolute expiration to null, we can get a cool effect of essentially dumping LRU objects every X hours, while extending the lifetime of objects we *do* need. This will hopefully fix a lot of issues, and will be a non-issue when this PR gets merged: https://github.com/Nihlus/Remora.Discord/pull/165

I can NOT express the reliquishment I felt when I finally narrowed down the actual cause of this issue. I've already brought it to the attention of the BCL team, as this behavior is somewhat unintuitive (sure, it makes sense if you actually access the object, but grrr)

A link to the issue is here: https://github.com/dotnet/runtime/issues/66445

---
## [IsaacLaquerre/WordleClone](https://github.com/IsaacLaquerre/WordleClone)@[ce7152f540...](https://github.com/IsaacLaquerre/WordleClone/commit/ce7152f54035ee6ad4b8ccc677f9d960ccb63ee8)
#### Thursday 2022-03-10 12:50:25 by IsaacLaquerre

Finished game. Word is not very secure but I tried my best by hashing compare requests. Plus you need to know about POST requests and how to make one to cheat and get the word. This is just a clone anyway, I don't know why I'm making such a big deal out of it. Oh look it's 7:49am and I stayed up all night. If you're reading this, have a good day... I'm going to go drown myself in coffee :)

---
## [ccp-eva/eyewit](https://github.com/ccp-eva/eyewit)@[8e73e25d0f...](https://github.com/ccp-eva/eyewit/commit/8e73e25d0fb6a29ea9f06aedf2be1ff1480f052b)
#### Thursday 2022-03-10 13:18:08 by Steven Kalinke

Fix hard-coded col names with variable ones... omg I hate myself

---
## [HermitDreams/FFR-Spellcrafting](https://github.com/HermitDreams/FFR-Spellcrafting)@[65f077b722...](https://github.com/HermitDreams/FFR-Spellcrafting/commit/65f077b722e6820df97ab70b1d9aac8ff1038bf8)
#### Thursday 2022-03-10 13:52:15 by Linkshot

Added March 10th's spell list (click for details)

CURE: Power: 16- Shape: Merging Stars, Colour: 10 (Bright Green), Message: 1 (HP up!) {WmRmWwRwKn}
JUG2: Power: 20, Acc Bonus: 62- Shape: Energy Bolt, Colour: 12 (Pale Cyan), Message: 0; None {WmWw}
JUDG: Power: 20, Acc Bonus: 59- Shape: Energy Bolt, Colour: 12 (Pale Cyan), Message: 0; None {WmWw}
SET : Acc Bonus: 236- Shape: Twinkles, Colour: 11 (Dark Green), Message: 29 (Defenseless) {WwRw}
-
SICK: Acc Bonus: 45 (Element: Poison)- Shape: Palm Blast, Colour: 4 (Purple), Message: 77 (Poison smoke) {BmBwRwNi}
ICE2: Power: 52, Acc Bonus: 8- Shape: Energy Flare, Colour: 13 (Bright Cyan), Message: 0; None {BmRmBwRwNi}
FIRE: Power: 25, Acc Bonus: 37- Shape: Energy Flare, Colour: 7 (Red), Message: 0; None {BmRmBwRwNi}
FAST- Shape: Bar of Light, Colour: 11 (Dark Green), Message: 18 (Quick shot) {BmBwRwNi}
=
FOG3: Power: 65- Shape: Twinkling Bar, Colour: 10 (Bright Green), Message: 2 (Armor up) {Ww}
FOG : Power: 16- Shape: Twinkling Bar, Colour: 10 (Bright Green), Message: 2 (Armor up) {WmWwRwKn}
ATOX- Shape: Twinkling Bar, Colour: 4 (Purple), Message: Defend aging {WmWwRwKn}
AICE- Shape: Twinkling Bar, Colour: 13 (Bright Cyan), Message: Defend cold {WmRmWwRwKn}
-
ARM : Power: 29- Shape: Bar of Light, Colour: 13 (Bright Cyan), Message: 2 (Armor up) {Bw}
SOOT: Acc Bonus: 38- Shape: Palm Blast, Colour: 7 (Red), Message: 0; None {BmRmBwRwNi}
ICE : Power: 44, Acc Bonus: 14- Shape: Energy Flare, Colour: 13 (Bright Cyan), Message: 0; None {BmRmBwRwNi}
POX : Acc Bonus: 54 (Element: Poison)- Shape: Palm Blast, Colour: 4 (Purple), Message: 77 (Poison smoke) {BmBwRwNi}
=
CUR2: Power: 33- Shape: Merging Stars, Colour: 12 (Pale Cyan), Message: 1 (HP up!) {WmRmWwRwKn}
AWEK- Shape: Twinkling Bar, Colour: 6 (Magenta), Message: Defend weak {WmRmWwRwKn}
VOXa- Shape: Magic Burst, Colour: 2 (Light Blue), Message: 0; None {WmWwRwKn}
HEAL: Power: 12- Shape: Stars, Colour: 10 (Bright Green), Message: 1 (HP up!) {WmWw}
-
WREK: Acc Bonus: 16- Shape: Flaring Bolt, Colour: 1 (White), Message: 0; None {BmBw}
SABR: Power: 21- Shape: Bar of Light, Colour: 2 (Light Blue), Message: 10 (Weapons stronger) {BmBwRwNi}
PIT : Power: 57, Acc Bonus: 26- Shape: Twinkles, Colour: 8 (Orange), Message: 5 (Easy to hit) {BmBwRwNi}
PIT2: Power: 95, Acc Bonus: 18- Shape: Twinkles, Colour: 8 (Orange), Message: 5 (Easy to hit) {BmBwRwNi}
=
PURE- Shape: Directed Burst, Colour: 10 (Bright Green), Message: 0; None {WmRmWwRw}
LMPa- Shape: Magic Burst, Colour: 7 (Red), Message: 0; None {WmWwRw}
INVS: Power: 39- Shape: Twinkling Bar, Colour: 3 (Dark Blue), Message: 3 (Easy to dodge) {WmRmWwRw}
ARUB- Shape: Twinkling Bar, Colour: 6 (Magenta), Message: Defend magic {WmWwRw}
-
VOLT: Power: 100, Acc Bonus: 31- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None {Bw}
LIT2: Power: 65, Acc Bonus: 21- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None {BmBwRwNi}
DCAY: Power Word (Element: Fire)- Shape: Sparkling Bolt, Colour: 7 (Red), Message:77 (Poison smoke) {BmBwRwNi}
HEX : Acc Bonus: 58 (Element: Status)- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None {BmRmBwRwNi}
=
CUR3: Power: 66- Shape: Merging Stars, Colour: 13 (Bright Cyan), Message: 1 (HP up!) {WmRmWwRw}
LIFE- Shape: Directed Burst, Colour: 12 (Pale Cyan), Message: 74 (Ineffective now) {WmWwRw}
ADMG- Shape: Twinkling Bar, Colour: 2 (Light Blue), Message: Defend spell {WmWwRw}
HEL2: Power: 24- Shape: Stars, Colour: 12 (Pale Cyan), Message: 1 (HP up!) {WmWw}
-
BSRK- Shape: Bar of Light, Colour: 6 (Magenta), Message:18 (Quick Shot) {BmRmBwRw}
SNOW: Power: 94, Acc Bonus: 63- Shape: Fizzling Flare, Colour: 13 (Bright Cyan), Message: 0; None {Bw}
WARP {BwRw}
MELT: Acc Bonus: 96- Shape: Glowing Ball, Colour: 7 (Red), Message: 21 (Erased) {Bw}
=
SOFT- Shape: Directed Burst, Colour: 1 (White), Message: 74 (Ineffective now) {WmWw}
EXIT {WwRw}
BLND: Power Word (Element: Status)- Shape: Sparkling Bolt, Colour: 6 (Magenta), Message: 0; None {WmWw}
FOG2: Power: 33- Shape: Twinkling Bar, Colour: 10 (Bright Green), Message: 2 (Armor up) {Ww}
-
CURS: Acc Bonus: 16 (Element: None)- Shape: Palm Blast, Colour: 9 (Yellow), Message: 0; None {BmRmBwRw}
DIM : Acc Bonus: 27- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None {BmRmBwRw}
HIDE: Power: 54- Shape: Bar of Light, Colour: 4 (Purple), Message: 3 (Easy to dodge) {BmRmBwRw}
GYSR: Power: 79, Acc Bonus: 116- Shape: Fizzling Flare, Colour: 9 (Yellow), Message: 0; None {BmRmBwRw}
=
MAX - Shape: Merging Stars, Colour: 3 (Dark Blue), Message: 24 (HP max!) {Ww}
STOP: Acc Bonus: 51- Shape: Palm Blast, Colour: 11 (Dark Green), Message: 30 (Time stopped) {RmWwRw}
HRM2: Power: 85, Acc Bonus: 25- Shape: Flaring Bolt, Colour: 12 (Pale Cyan), Message: 0; None {Ww}
HEL3: Power: 48- Shape: Stars, Colour: 13 (Bright Cyan), Message: 1 (HP up!) {WmWw}
-
HIB : Acc Bonus: 29- Shape: Palm Blast, Colour: 13 (Bright Cyan), Message: 76 (Frozen) {BmRmBwRw}
LIT : Power: 30, Acc Bonus: 19- Shape: Flaring Bolt, Colour: 3 (Dark Blue), Message: 0; None {BmRmBwRw}
SHOK: Power: 57, Acc Bonus: 39- Shape: Energy Bolt, Colour: 3 (Dark Blue), Message: 0; None {BmRmBwRw}
GLAC: Power: 44, Acc Bonus: 36- Shape: Twinkles, Colour: 13 (Bright Cyan), Message: 5 (Easy to hit) {BmRmBwRw}
=
LIF2- Shape: Merging Stars, Colour: 5 (Pink), Message: 74 (Ineffective now) {Ww}
HARM: Power: 84, Acc Bonus: 29- Shape: Flaring Bolt, Colour: 12 (Pale Cyan), Message: 0; None {Ww}
MUTE: Acc Bonus: 46- Shape: Palm Blast, Colour: 6 (Magenta), Message: 0; None {RmWwRw}
BLES: Power: 14, Acc Bonus: 58- Shape: Bar of Light, Colour: 12 (Pale Cyan), Message: 27 (Weapon became enchanted) {Ww}
-
ROT : Power: 114, Acc Bonus: 60- Shape: Fizzling Flare, Colour: 14 (Grey), Message: 0; None {Bw}
PURG: Acc Bonus: 27- Shape: Twinkles, Colour: 9 (Yellow), Message: 29 (Defenseless) {RmBwRw}
AGE : Acc Bonus: 76- Shape: Twinkles, Colour: 11 (Dark Green), Message: 11 (Lost intelligence) {BwRw}
HYDR: Power: 87, Acc Bonus: 7- Shape: Fizzling Flare, Colour: 2 (Light Blue), Message: 0; None {BwRw}
=
Battle Messages
#01: HP up! [Assigned]
#02: Armor up [Assigned]
#03: Easy to dodge [Assigned]
#05: Easy to hit [Assigned]
#08: Defend futility [Spaces to add: 1]
#10: Weapons stronger [Assigned]
#11: Lost intelligence [Assigned]
#12: Defend cold
#13: Attack halted [Unassigned]
#15: Became terrified [Unassigned]
#16: Defend weak
#18: Quick shot [Assigned]
#21: Erased [Assigned]
#22: Fell into crack [Unassigned]
#24: HP max! [Assigned]
#25: Defend magic
#27: Weapon became enchanted [Assigned]
#28: Defend wiz
#29: Defenseless [Assigned]
#30: Time stopped [Assigned]
#31: Exile to 4th dimension [Unassigned]
#43: Critical hit!! [Unassigned]
#47: Stopped [Unassigned]
#74: Ineffective now [Assigned]
#76: Frozen
#77: Poison smoke [Assigned]

---
## [Gandalf2k15/tgstation](https://github.com/Gandalf2k15/tgstation)@[3bd5a2d8df...](https://github.com/Gandalf2k15/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Thursday 2022-03-10 14:20:16 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[52e64c50ce...](https://github.com/repinger/exynos9611_m21_kernel/commit/52e64c50ce0a08ede93bf0734d37d41ba6f2fde6)
#### Thursday 2022-03-10 14:24:20 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [pixeltrix/rails](https://github.com/pixeltrix/rails)@[4e7cfbfcfd...](https://github.com/pixeltrix/rails/commit/4e7cfbfcfd69e1398ccfa74e71aa1eca19eef5bf)
#### Thursday 2022-03-10 14:41:43 by Sean Griffin

Don't assume all hashes are from multiparameter assignment in `composed_of`

So this bug is kinda funky. The code path is basically "if we weren't passed an
instance of the class we compose to, and we have a converter, call that".
Ignoring the hash case for a moment, everything after that was roughly intended
to be the "else" clause, meaning that we are expected to have an instance of
the class we compose to. Really, we should be blowing up in that case, as we
can give a much better error message than what they user will likely get (e.g.
`NameError: No method first for String` or something). Still, Ruby is duck
typed, so if the object you're assigning responds to the same methods as the
type you compose to, knock yourself out.

The hash case was added in 36e9be8 to remove a bunch of special cased code from
multiparameter assignment. I wrongly assumed that the only time we'd get a hash
there is in that case. Multiparameter assignment will construct a very specific
hash though, where the keys are integers, and we will have a set of keys
covering `1..part.size` exactly. I'm pretty sure this could actually be passed
around as an array, but that's a different story. Really I should convert this
to something like `class MultiParameterAssignment < Hash; end`, which I might
do soon. However for a change that I'm willing to backport to 4-2-stable, this
is what I want to go with for the time being.

Fixes #25978

---
## [DexterHuang/CyberCodeOnline](https://github.com/DexterHuang/CyberCodeOnline)@[6d5cb134f2...](https://github.com/DexterHuang/CyberCodeOnline/commit/6d5cb134f217d2cfa2a14edfd3a81d4748a74fdc)
#### Thursday 2022-03-10 14:52:17 by S0M3_DUD3

Updated german commen used curse words

Translations
		"Arschfresse" - Analface
		"Arschlecker" - Anallicker
		"Arschficker" - Analfucker
		"Pimmel" - other word for dick
		"Schwanzlutscher" - dicksucker
		"Kanacke" - curse word for imigrants
		"Fettsack" - "Fat guy"
		"Schlampe" - "Bitch"
		"Mutterficker" - "Motherfucker"
		"Assi" - curse word for jobless
		"Aushilfsnazi" - nazi thing

---
## [elastic/elasticsearch](https://github.com/elastic/elasticsearch)@[37ea6a8255...](https://github.com/elastic/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Thursday 2022-03-10 15:05:47 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [huggingface/datasets](https://github.com/huggingface/datasets)@[a8fa7cfe95...](https://github.com/huggingface/datasets/commit/a8fa7cfe95e06c8a667c4d7c5b7c7287b7e9ac4f)
#### Thursday 2022-03-10 15:30:39 by RenChu Wang

Multi-GPU support for `FaissIndex` (#3721)

* 🎉 This commit fixes huggingface/datasets#3716

This commit adds handling for faiss indices that run on multiple GPUs.

* 🤕 Stupid mistake in that index isn't returned in the function handling device.

Now it's fixed. Hopefully the PR isn't merged yet!

* 🗎 Updated documents to reflect changes I made in the code.

Update `device`'s document to include negative numbers and lists.

* 1️⃣ The line should not exceed length: 119

It seems that this is what circle CI checked anyways.

* 🥴 Apply suggestions from code review

Missed it the first time :)

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>

* 🛠️ Fixed my fixes.

Updated code to address concerns.

* 🇫 Update src/datasets/search.py

Using f-strings in docs.

Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>
Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

---
## [teotm/lyrical-file-support-for-fnf](https://github.com/teotm/lyrical-file-support-for-fnf)@[229b7c911e...](https://github.com/teotm/lyrical-file-support-for-fnf/commit/229b7c911edcd11d75d4d8631d92147c5245e518)
#### Thursday 2022-03-10 15:56:16 by KolczatkowyToNieJestPrzymiotnik

fuckin shit

if you'll make a drama about it that i swear go to child adoption store. fnf is not a kids game.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Thursday 2022-03-10 15:59:10 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [MinArchie/Shithole](https://github.com/MinArchie/Shithole)@[a44e1621a2...](https://github.com/MinArchie/Shithole/commit/a44e1621a23fedbdac7099088572202c77661d0b)
#### Thursday 2022-03-10 16:01:05 by MinArchie

IGNORE PREVIOUS!! "finished ver"

THIS ONE is the finished ver. the other one had a mistake lol. anyway if you get time pleaseee look through it to find any bugs. and I did a horrible job of centering and placing the text and buttons so forgive me

---
## [Pemseles/Analysis-Year-2-Coding](https://github.com/Pemseles/Analysis-Year-2-Coding)@[c54fab0e53...](https://github.com/Pemseles/Analysis-Year-2-Coding/commit/c54fab0e53f88aeed1db40d7afa67c31b9441e9b)
#### Thursday 2022-03-10 16:21:37 by Pemseles

furthering my w0rk

card effects fucking suck my peewee holy shit aaaAAAAAAAAA

---
## [avar/git](https://github.com/avar/git)@[d28cec5691...](https://github.com/avar/git/commit/d28cec569186a7fed662bb62fa53b5fe4fc49262)
#### Thursday 2022-03-10 16:28:49 by Ævar Arnfjörð Bjarmason

usage API: use C99 macros for {usage,usagef,die,error,warning,die}*()

Change the "usage" family of functions to be defined in terms of C99
variadic macros, as we've optionally done with the BUG() macro and
BUG_fl() function since d8193743e08 (usage.c: add BUG() function,
2017-05-12), and unconditionally since 765dc168882 (git-compat-util:
always enable variadic macros, 2021-01-28).

This would have been possible before having a hard dependency on C99,
but as the dual implementations of C99 and pre-C99 macros and
functions adjusted in preceding commits show, doing so would have been
rather painful.

By having these be macros we'll now log meaningful "file" and "line"
entries in trace2 events. Before this we'd log "usage.c" in all of
them, and the line would be the relevant locations in that file.

To do this we need to not only introduce X_fl() functions for
{die,error,warning,die}{,_errno}(), but also change all the callers of
the set_*() and get_() functions in usage.h to take "file" and "line"
arguments.

Neither the built-in {die,error,warning,die}{,_errno}() nor anyone
else does anything useful with these "file" and "line" arguments for
now, but it means we can define all our macros and functions
consistently.

It also opens the door for a follow-up change where these functions
could optionally emit the file name and line number, e.g. for
DEVELOPER=1 builds, or depending on configuration.

It might be a good change to remove the "fmt" key from the "error"
events as a follow-up change. As these few examples from running the
test suite show it's sometimes redundant (same as the "msg"), rather
useless (just a "%s"), or something we could now mostly aggregate by
file/line instead of the normalized printf format:

      1 file":"builtin/gc.c","line":1391,"msg":"'bogus' is not a valid task","fmt":"'%s' is not a valid task"}
      1 file":"builtin/for-each-ref.c","line":89,"msg":"format: %(then) atom used more than once","fmt":"%s"}
      1 file":"builtin/fast-import.c","line":411,"msg":"Garbage after mark: N :202 :302x","fmt":"Garbage after mark: %s"}

"Mostly" here assumes that it would be OK if the aggregation changed
between git versions, which may be what all users of trace2 want. The
change that introduced the "fmt" code was ee4512ed481 (trace2: create
new combined trace facility, 2019-02-22), and the documentation change
was e544221d97a (trace2: Documentation/technical/api-trace2.txt,
2019-02-22).

Both are rather vague on what problem "fmt" solved exactly, aside from
the obvious one of it being impossible to do meaningful aggregations
due to the "file" and "line" being the same everywhere, which isn't
the case now.

In any case, let's leave "fmt" be for now, the above summary was given
in case it's interesting to remove it in the future, e.g. to save
space in trace2 payloads.

The change here in git_die_config() is the bare minimum needed to get
it working, but better would be a change[1] to correctly report the
caller file and line numbers. Let's leave that for later, it can be
done later.

1. https://lore.kernel.org/git/patch-4.4-e0e6427cbd3-20211206T165221Z-avarab@gmail.com/#t

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[0e6fb6726a...](https://github.com/avar/git/commit/0e6fb6726acfe46a6fa82ac26e571ea7c4d63b56)
#### Thursday 2022-03-10 16:29:19 by Ævar Arnfjörð Bjarmason

usage API: make the "{usage,fatal,error,warning,BUG}: " translatable

In preceding commits the vreportf() function was made static, so we
know it's only being called with a limited set of fixed prefixes. Pass
an enum indicating the kind of usage message we're emitting instead,
which means that we can fold the BUG_vfl_common() functionality
directly into it.

Since we've now got one place were we're emitting these usage messages
we can make them translatable.

We need to be careful with this function to not malloc() anything, as
a failure in say a use of strbuf_vaddf() would call xmalloc(), which
would in turn call die(), but here we're using static strings, either
from libintl or not.

I was on the fence about making the "BUG: " message translatable, but
let's do it for consistency. Someone who doesn't speak a word of
English may not know what "BUG" means, but if it's translated they
might have an easier time knowing that they have to report a bug
upstream. Since we'll always emit the line number it's unlikely that
we're going to be confused by such a report.

As we've moved the BUG_vfl_common() code into vsnprintf() we can do
away with one of the two checks for buffer sizes added in
116d1fa6c69 (vreportf(): avoid relying on stdio buffering, 2019-10-30)
and ac4896f007a (fmt_with_err: add a comment that truncation is OK,
2018-05-18).

I.e. we're being overly paranoid if we define the fixed-size "prefix"
and "msg" buffers, are OK with the former being truncated, and then
effectively check if our 256-byte buffer is larger than our 4096-byte
buffer. I wondered about adding a:

    assert(sizeof(prefix) < sizeof(msg)); /* overly paranoid much? */

But I think that would be overdoing it. Anyone modifying this function
will keep these two buffer sizes in mind, so let's just remove one of
the checks instead.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[8e09838821...](https://github.com/avar/git/commit/8e09838821a5cc5faf48634ea1fed51fe38b4056)
#### Thursday 2022-03-10 16:29:27 by Ævar Arnfjörð Bjarmason

usage API: add "core.usageAddSource" config to add <file>:<line>

Optionally extend the support that BUG() has had for emitting line
numbers to the {usage,fatal,error,warning}{,_errno}() functions.

Before we'd unconditionally get error messages like:

    $ git -c core.x=y config --get --bool core.x
    fatal: bad boolean config value 'y' for 'core.x'

Which can be changed with core.usageAddSource=true to include the file
and line numbers:

    $ git -c core.usageAddSource=true -c core.x=y config --get --bool core.x
    fatal: config.c:1241: bad boolean config value 'y' for 'core.x'

As the added documentation notes this is primarily intended to be
useful to developers of git itself, but is being exposed as a user
setting to e.g. help file better bug reports.

This also adds a "GIT_TEST_USAGE_ADD_SOURCE" setting intended to run
the test suite in this mode.

Currently it has a lot of failures. Most of those are rather trivial,
and can be "fixed" by pointing GIT_TEST_CMP to a "diff -u" that does a
s/^(usage|fatal|error|warning): [^:]+:[0-9]+/$1/g on its input files,
and likewise for a "grep" wrapper that does the same.

Even if we can't run the tests in this mode yet I'd like to have this
for ad-hoc debugging, and to make it easier to work towards running
the tests in this mode. If we can turn this on permanently it'll be
much easier to read test output, as we won't need to worry about the
indirection of looking up where an error might have been emitted,
which can be especially painful when the message being emitted isn't
unique within git.git.

This new code needs to be guarded by the "dying" variable for the
reasons explained in 2d3c02f5db6 (die(): stop hiding errors due to
overzealous recursion guard, 2017-06-21), and for those same reasons
it's racy under multi-threading.

Here the worst case is that incrementing the variable will run away
from us, and we won't get our desired <file>:<line> number. That's OK
in this case, those cases should be isolated to the config code (if we
can't parse the config), memory allocation etc, but we'll get it right
in the common cases.

Using GIT_TEST_USAGE_ADD_SOURCE should be immune from any racyness, as
it only needs a getenv() and git_parse_maybe_bool(), which won't die.

Add a repo_cfg_bool_env() wrapper to repo-settings.c for
GIT_TEST_USAGE_ADD_SOURCE, in 3050b6dfc75 (repo-settings.c: simplify
the setup, 2021-09-21) I indicated that the GIT_TEST_MULTI_PACK_INDEX
env variable/config pair in that file has odd semantics, but users of
repo_cfg_bool_env() have straightforward and expected semantics. If
the environment variable is set (true or false) we'll use it,
otherwise we'll use the config, and finally fall back on the
default (of "false", in this case).

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [BoHBranch/BoH-Bay](https://github.com/BoHBranch/BoH-Bay)@[e949b98d60...](https://github.com/BoHBranch/BoH-Bay/commit/e949b98d60d0cf6f2bfceac3c6453b3fbf61e309)
#### Thursday 2022-03-10 16:29:38 by Pariah919

Ports gun attachments (#1250)

* i hate technobug

* Update gun.dm

* ok

* attachments work again

* yeah, I never added these sounds, and?

ping mjp#4043 on discord if these sounds are still not added when i wake up in 4 hours and are avaliabel

* ye

* attachments moment

* howdoesthisnotruntime

* comment less agressive, sorry

* attachies

Co-authored-by: Carl? <Stats-and-tracks@hotmail.com>

---
## [maheshsal/linux-ci](https://github.com/maheshsal/linux-ci)@[a50e1fcbc9...](https://github.com/maheshsal/linux-ci/commit/a50e1fcbc9b85fd4e95b89a75c0884cb032a3e06)
#### Thursday 2022-03-10 16:41:25 by Josef Bacik

btrfs: do not WARN_ON() if we have PageError set

Whenever we do any extent buffer operations we call
assert_eb_page_uptodate() to complain loudly if we're operating on an
non-uptodate page.  Our overnight tests caught this warning earlier this
week

  WARNING: CPU: 1 PID: 553508 at fs/btrfs/extent_io.c:6849 assert_eb_page_uptodate+0x3f/0x50
  CPU: 1 PID: 553508 Comm: kworker/u4:13 Tainted: G        W         5.17.0-rc3+ #564
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.13.0-2.fc32 04/01/2014
  Workqueue: btrfs-cache btrfs_work_helper
  RIP: 0010:assert_eb_page_uptodate+0x3f/0x50
  RSP: 0018:ffffa961440a7c68 EFLAGS: 00010246
  RAX: 0017ffffc0002112 RBX: ffffe6e74453f9c0 RCX: 0000000000001000
  RDX: ffffe6e74467c887 RSI: ffffe6e74453f9c0 RDI: ffff8d4c5efc2fc0
  RBP: 0000000000000d56 R08: ffff8d4d4a224000 R09: 0000000000000000
  R10: 00015817fa9d1ef0 R11: 000000000000000c R12: 00000000000007b1
  R13: ffff8d4c5efc2fc0 R14: 0000000001500000 R15: 0000000001cb1000
  FS:  0000000000000000(0000) GS:ffff8d4dbbd00000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 00007ff31d3448d8 CR3: 0000000118be8004 CR4: 0000000000370ee0
  Call Trace:

   extent_buffer_test_bit+0x3f/0x70
   free_space_test_bit+0xa6/0xc0
   load_free_space_tree+0x1f6/0x470
   caching_thread+0x454/0x630
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? lock_release+0x1f0/0x2d0
   btrfs_work_helper+0xf2/0x3e0
   ? lock_release+0x1f0/0x2d0
   ? finish_task_switch.isra.0+0xf9/0x3a0
   process_one_work+0x26d/0x580
   ? process_one_work+0x580/0x580
   worker_thread+0x55/0x3b0
   ? process_one_work+0x580/0x580
   kthread+0xf0/0x120
   ? kthread_complete_and_exit+0x20/0x20
   ret_from_fork+0x1f/0x30

This was partially fixed by c2e39305299f01 ("btrfs: clear extent buffer
uptodate when we fail to write it"), however all that fix did was keep
us from finding extent buffers after a failed writeout.  It didn't keep
us from continuing to use a buffer that we already had found.

In this case we're searching the commit root to cache the block group,
so we can start committing the transaction and switch the commit root
and then start writing.  After the switch we can look up an extent
buffer that hasn't been written yet and start processing that block
group.  Then we fail to write that block out and clear Uptodate on the
page, and then we start spewing these errors.

Normally we're protected by the tree lock to a certain degree here.  If
we read a block we have that block read locked, and we block the writer
from locking the block before we submit it for the write.  However this
isn't necessarily fool proof because the read could happen before we do
the submit_bio and after we locked and unlocked the extent buffer.

Also in this particular case we have path->skip_locking set, so that
won't save us here.  We'll simply get a block that was valid when we
read it, but became invalid while we were using it.

What we really want is to catch the case where we've "read" a block but
it's not marked Uptodate.  On read we ClearPageError(), so if we're
!Uptodate and !Error we know we didn't do the right thing for reading
the page.

Fix this by checking !Uptodate && !Error, this way we will not complain
if our buffer gets invalidated while we're using it, and we'll maintain
the spirit of the check which is to make sure we have a fully in-cache
block while we're messing with it.

CC: stable@vger.kernel.org # 5.4+
Signed-off-by: Josef Bacik <josef@toxicpanda.com>
Signed-off-by: David Sterba <dsterba@suse.com>

---
## [VinayTambey/My_Github_Journey](https://github.com/VinayTambey/My_Github_Journey)@[d9e0daf4df...](https://github.com/VinayTambey/My_Github_Journey/commit/d9e0daf4dfa2beda03f14cfbda1428360205eb60)
#### Thursday 2022-03-10 16:59:58 by Vinay Tambey

Tip Calculator

Hey, this is my 9th project, which is based on a real life problem, where you can use this program as a tip calculator, when you have gone to a hotel or restaurant to have tasty foods or meals with your friends or family members but having problem that or getting confused that "how much tip we should give?", so there you can use this tip calculator.

---
## [Perl/perl5](https://github.com/Perl/perl5)@[c155bccb38...](https://github.com/Perl/perl5/commit/c155bccb38ea16f0b80b5a69c812548165010fdb)
#### Thursday 2022-03-10 17:05:58 by Yves Orton

Create Porting/MANIFEST.dev as a complement to MANIFEST and related infra

This file is intended to list all the files in the repo which are not
listed in the main MANIFEST file, and which are used only for
development purposes, especially those files which are only useful when
working in a git checkout of the main perl git repository.

The files it contains will NOT be added to the production tarball
release. The file has the exact same format as the main MANIFEST:
"file\t+description" or "file".

Q. Why didn't I call this Porting/MANIFEST as mentioned in the
   discussion thread that lead to this patch?

A. The main reason was that Porting/README.pod includes a list of files
   in Porting with descriptions and explanations for what the files do
   or how they are used. In several places the file refers to
   "MANIFEST", which lead to ambiguity that would have had to be
   resolved by changing all the entries to refer to "Porting/whatever"
   instead. It was much simpler to give the new file an extension, and I
   thought that '.dev' suggests it is for "development" purposes.

Q. Why isn't this using MANIFEST.skip style functionality?

A1. Various parts of our build and test process expect to read the
    MANIFEST file and then do things based on the entries contained
    within. Eg, run tests, or extract data, or compare the file list to
    content in another file. Those parts of our build process would
    break if we used a skip style list of regexen. So it would be more
    work to teach them to deal with such a file, assuming it was
    actually doable - given the additional work I have not considered it
    deeply. On the other hand teaching that logic to simply read two
    files was and is easy.

A2. I think each file we have in the repo should have a description.
    This patch currently doesn't provide a description for each, but it
    does for many, especially those migrated from MANIFEST.

A3. I think that MANIFEST.skip style files of exclusion regexens and
    globs are error prone and easy to mess up, for instance by excluding
    far more than you had intended to. They can also be annoying to get
    right, obviously not impossible, but sometimes annoying. Explicitly
    listing everything is easy in every way, especially to mechanize.

A4. I would like to be able to move verbatim entries from our existing
    MANIFEST into the new Porting/MANIFEST.dev, description and all.
    MANIFEST.skip style files do not support descriptions except as
    comments as far as I recall. That would have meant munging the data
    from MANIFEST during the move process which would be annoying.

A5. I would like to be able to reuse our sorting logic to keep the files
    nicely sorted in a way where the file is somewhat readable. A list
    of skip files would be less amenable to doing so.

Q. There is a lot of duplicated logic related to manifests, should we
   refactor it out into a module or some resuable tool set?

A. YES! We already have Porting/manifest_lib.pm, but it currently does
   not declare a package, and it only contains one function. Instead of
   adding yet more code that depends on requiring a file and having it
   inject subs into package main I decided that doing the refactoring
   could wait for a separate commit or PR. But I definitely think we
   should refactor as much of this logic as possible.

Q. Some of the test files were fairly significantly changed, are you
   sure you didn't break or drop any of the tests?

A. I am reasonably confident I did not. Secondary review appreciated.
   Some of the touched files are quite old and obviously "quick hack"
   scripts. By rewriting them quite a bit I was able to simplify and
   perform some of the tests in different ways or parts of the script.
   As far as I know I didn't drop any.

Q. Why didn't you use newer features in the rewrite?

A. I am a bit conservative in my taste, and I like build tools to be
   able to run on older perls, and for things like this I prefer to
   stick with what I know well. Patches welcome.

Q. Why didn't you move more of the stuff we shouldn't bundle with
   our releases?

A. I figured someone like Nicolas R. (who helped motivate this patch)
   would feel left out if I didn't leave him anything to do. :-)

---
## [asus-sdm660-devs/android_kernel_asus_sdm660](https://github.com/asus-sdm660-devs/android_kernel_asus_sdm660)@[ded92fc938...](https://github.com/asus-sdm660-devs/android_kernel_asus_sdm660/commit/ded92fc93845f9906d2f3b1482f80856d8bb6528)
#### Thursday 2022-03-10 17:52:37 by Maciej Żenczykowski

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
## [alexander-akait/next.js](https://github.com/alexander-akait/next.js)@[91146b23a2...](https://github.com/alexander-akait/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Thursday 2022-03-10 17:59:16 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [ubarilan/ldcona](https://github.com/ubarilan/ldcona)@[16ddf999b0...](https://github.com/ubarilan/ldcona/commit/16ddf999b036ffbfa8df9a2d77271c8609747bdb)
#### Thursday 2022-03-10 20:30:43 by AsafSivan1

idc it doesn't work i worked so much about it and i don't give af about the errors so fuck your typescript

---
## [TerraLindaHighSchool/memorium-memorium-production-team](https://github.com/TerraLindaHighSchool/memorium-memorium-production-team)@[97ed4ef350...](https://github.com/TerraLindaHighSchool/memorium-memorium-production-team/commit/97ed4ef35003ac75fbc7f016dd93a6b2599de8ec)
#### Thursday 2022-03-10 20:55:15 by WoofMeister

i hate you stupid github you need to die jk lol not really haha funny also i put angyboi inside unity bc hawt

---
## [EnderDev/EnderDev](https://github.com/EnderDev/EnderDev)@[5637398fda...](https://github.com/EnderDev/EnderDev/commit/5637398fda872b75cb97e6e18ced026594c91898)
#### Thursday 2022-03-10 21:11:08 by EnderDev-robot

A man is smoking a cigarette and blowing smoke rings into the air. His girlfriend becomes irritated with the smoke and says \"Can't you see the warning on the cigarette pack? Smoking is hazardous to your health!\" to which the man replies, \"I am a programmer.  We don't worry about warnings; we only worry about errors.\"

---
## [EnderDev/EnderDev](https://github.com/EnderDev/EnderDev)@[893e0d8386...](https://github.com/EnderDev/EnderDev/commit/893e0d83861ddd34c163f2ffd052d3ee48d1f7f7)
#### Thursday 2022-03-10 21:12:26 by EnderDev-robot

A man is smoking a cigarette and blowing smoke rings into the air. His girlfriend becomes irritated with the smoke and says "Can't you see the warning on the cigarette pack? Smoking is hazardous to your health!" to which the man replies, "I am a programmer.  We don't worry about warnings; we only worry about errors."

---
## [spinnakerbot/gate](https://github.com/spinnakerbot/gate)@[e2a108db75...](https://github.com/spinnakerbot/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Thursday 2022-03-10 21:25:31 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---

