## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-23](docs/good-messages/2023/2023-09-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,976,713 were push events containing 2,748,455 commit messages that amount to 163,048,957 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [arp242/toml](https://github.com/arp242/toml)@[c3b534eb89...](https://github.com/arp242/toml/commit/c3b534eb892c7c81480463333cd775db13737c82)
#### Saturday 2023-09-23 00:07:24 by Martin Tournoij

Change bare key characters to Letter and Digit

I believe this would greatly improve things and solves all the issues,
mostly. It's a bit more complex, but not overly so, and can be
implemented without a Unicode library without too much effort. It offers
a good middle ground, IMHO.

I don't think there are ANY perfect solutions here and that *anything*
will be a trade-off. That said, I do believe some trade-offs are better
than others, and after looking at a bunch of different options I believe
this is by far the best path for TOML.

Advantages:

- This is what I would consider the "minimal set" of characters we need
  to add for reasonable international support, meaning we can't really
  make a mistake with this by accidentally allowing too much.

  We can add new ranges in TOML 1.2 (or even change the entire approach,
  although I'd be very surprised if we need to), based on actual
  real-world feedback, but any approach we will take will need to
  include letters and digits from all scripts.

  This is a strong argument in favour of this and a huge improvement: we
  can't really do anything wrong here in a way that we can't correct
  later. Being conservative for these type of things is is good!

- This solves the normalisation issues, since combining characters are
  no longer allowed in bare keys, so it becomes a moot point.

  For quoted keys normalisation is mostly a non-issue because few people
  use them and the specification even strongly discourages people from
  using them, which is why this gone largely unnoticed and undiscussed
  before the "Unicode in bare keys" PR was merged.[1]

- It's consistent in what we allow: no "this character is allowed, but
  this very similar other thing isn't, what gives?!"

  Note that #954 was NOT about "I want all emojis to work" per se, but
  "this character works fine, but this very similar doesn't". This shows
  up in a number of things aside from emojis:

      a.toml:
              Input:   ; = 42  # U+037E GREEK QUESTION MARK (Other_Punctuation)
              Error:   line 1: expected '.' or '=', but got ';' instead

      b.toml:
              Input:   · = 42  # # U+0387 GREEK ANO TELEIA (Other_Punctuation)
              Error:   (none)

      c.toml:
              Input:   – = 42  # U+2013 EN DASH (Dash_Punctuation)
              Error:   line 1: expected '.' or '=', but got '–' instead

      d.toml:
              Input:   ⁻ = 42  # U+207B SUPERSCRIPT MINUS (Math_Symbol)
              Error:   (none)

      e.toml:
              Input:   ＃x = "commented ... or is it?"  # # U+FF03 FULLWIDTH NUMBER SIGN (Other_Punctuation)
              Error:   (none)

  "Some punctuation is allowed but some isn't" is hard to explain, and
  also not what the specification says: "Punctuation, spaces, arrows,
  box drawing and private use characters are not allowed." In reality, a
  lot of punctuation IS allowed, but not all.

  People don't read specifications, nor should they. People try
  something and sees if it works. Now it seems to work on first
  approximation, and then (possibly months later) it seems to "break".

  It should either allow everything or nothing. This in-between is just
  horrible. From the user's perspective this seems like a bug in the
  TOML parser, but it's not: it's a bug in the specification.

  There is no good way to communicate this other than "these codepoints,
  which cover most of what you'd write in a sentence, except when it
  doesn't".

  In contrast, "we allow letters and digits" is simple to spec, simple
  to communicate, and should have a minimum potential for confusion. The
  current spec disallows some things seemingly almost arbitrary while
  allowing other very similar characters.

- This avoids a long list of confusable special TOML characters; some
  were mentioned above but there are many more:

      '＃' U+FF03     FULLWIDTH NUMBER SIGN (Other_Punctuation)
      '＂' U+FF02     FULLWIDTH QUOTATION MARK (Other_Punctuation)
      '﹟' U+FE5F     SMALL NUMBER SIGN (Other_Punctuation)
      '﹦' U+FE66     SMALL EQUALS SIGN (Math_Symbol)
      '﹐' U+FE50     SMALL COMMA (Other_Punctuation)
      '︲' U+FE32     PRESENTATION FORM FOR VERTICAL EN DASH (Dash_Punctuation)
      '˝'  U+02DD     DOUBLE ACUTE ACCENT (Modifier_Symbol)
      '՚'  U+055A     ARMENIAN APOSTROPHE (Other_Punctuation)
      '܂'  U+0702     SYRIAC SUBLINEAR FULL STOP (Other_Punctuation)
      'ᱹ'  U+1C79     OL CHIKI GAAHLAA TTUDDAAG (Modifier_Letter)
      '₌'  U+208C     SUBSCRIPT EQUALS SIGN (Math_Symbol)
      '⹀'  U+2E40     DOUBLE HYPHEN (Dash_Punctuation)
      '࠰'  U+0830     SAMARITAN PUNCTUATION NEQUDAA (Other_Punctuation)

  Is this a big problem? I guess it depends; I can certainly imagine an
  Armenian speaker accidentally leaving an Armenian apostrophe.

- Maps to identifiers in more (though not all) languages. We discussed
  whether TOML keys are "strings" or "identifiers" last week in #966 and
  while views differ (mostly because they're both) it seems to me that
  making it map *closer* is better. This is a minor issue, but it's
  nice.

That does not mean it's perfect; as I mentioned all solutions come with
a trade-off. The ones made here are:

- The biggest issue by far is that the check to see if a character is
  valid may become more complex for some languages and environments that
  can't rely on a Unicode database being present.

  However, implementing this check is trivial logic-wise: it just needs
  to loop over every character and check if it's in a range table.

  The downside is it needs a somewhat large-ish "allowed characters"
  table with 716 start/stop ranges, which is not ideal, but entirely
  doable and easily auto-generated. It's ~164 lines hard-wrapped at
  column 80 (or ~111 lines hard-wrapped at col 120). tomlc99 is 2,387
  lines, so that seems within the limits of reason (actually, reading
  through the code adding multibyte support in the first case will
  probably be harder, with this range table being a minor part).

- There's a new Unicode version roughly every year or so, and the way
  it's written now means it's "locked" to Unicode 9 or, optionally, a
  later version. This is probably fine: Apple's APFS filesystem (which
  does normalisation) is "locked" to Unicode 9.0; HFS+ was Unicode 3.2.
  Go is Unicode 8.0. etc. I don't think this is really much of an issue
  in practice.

  I choose Unicode 9 as everyone supports this; I doubted a long time
  over it, and we can also use a more recent version. I feel this gives
  us a nice balance between reasonable interoperability while also
  future-proofing things.

- ABNF doesn't support Unicode. This is a tooling issue, and in my
  opinion the tooling should adjust to how we want TOML to look like,
  rather than adjusting TOML to what tooling supports. AFAIK no one uses
  the ABNF directly in code, and it's merely "informational".

  I'm not happy with this, but personally I think this should be a
  non-issue when considering what to do here. We're not the only people
  running in to this limitation, and is really something that IETF
  should address in a new RFC or something "Extra Augmented BNF?"

Another solution I tried is restricting the code ranges; I twice tried
to do this (with some months in-between) and spent a long time looking
at Unicode blocks and ranges, and I found this impractical: we'll end up
with a long list which isn't all that different from what this proposal
adds.

Fixes #954
Fixes #966
Fixes #979
Ref #687
Ref #891
Ref #941

---

[1]:
Aside: I encountered this just the other day as I created a TOML file
with all UK election results since 1945, which looks like:

     [1950]
     Labour       = [13_266_176, 315, 617]
     Conservative = [12_492_404, 298, 619]
     Liberal      = [ 2_621_487,   9, 475]
     Sinn_Fein    = [    23_362,   0,   2]

That should be Sinn_Féin, but "Sinn_Féin" seemed ugly, so I just wrote
it as Sinn_Fein. This is what most people seem to do.

---
## [alexbatashev/linux](https://github.com/alexbatashev/linux)@[3c919b0910...](https://github.com/alexbatashev/linux/commit/3c919b0910906cc69d76dea214776f0eac73358b)
#### Saturday 2023-09-23 00:11:51 by Darrick J. Wong

xfs: reserve less log space when recovering log intent items

Wengang Wang reports that a customer's system was running a number of
truncate operations on a filesystem with a very small log.  Contention
on the reserve heads lead to other threads stalling on smaller updates
(e.g.  mtime updates) long enough to result in the node being rebooted
on account of the lack of responsivenes.  The node failed to recover
because log recovery of an EFI became stuck waiting for a grant of
reserve space.  From Wengang's report:

"For the file deletion, log bytes are reserved basing on
xfs_mount->tr_itruncate which is:

    tr_logres = 175488,
    tr_logcount = 2,
    tr_logflags = XFS_TRANS_PERM_LOG_RES,

"You see it's a permanent log reservation with two log operations (two
transactions in rolling mode).  After calculation (xlog_calc_unit_res()
adds space for various log headers), the final log space needed per
transaction changes from  175488 to 180208 bytes.  So the total log
space needed is 360416 bytes (180208 * 2).  [That quantity] of log space
(360416 bytes) needs to be reserved for both run time inode removing
(xfs_inactive_truncate()) and EFI recover (xfs_efi_item_recover())."

In other words, runtime pre-reserves 360K of space in anticipation of
running a chain of two transactions in which each transaction gets a
180K reservation.

Now that we've allocated the transaction, we delete the bmap mapping,
log an EFI to free the space, and roll the transaction as part of
finishing the deferops chain.  Rolling creates a new xfs_trans which
shares its ticket with the old transaction.  Next, xfs_trans_roll calls
__xfs_trans_commit with regrant == true, which calls xlog_cil_commit
with the same regrant parameter.

xlog_cil_commit calls xfs_log_ticket_regrant, which decrements t_cnt and
subtracts t_curr_res from the reservation and write heads.

If the filesystem is fresh and the first transaction only used (say)
20K, then t_curr_res will be 160K, and we give that much reservation
back to the reservation head.  Or if the file is really fragmented and
the first transaction actually uses 170K, then t_curr_res will be 10K,
and that's what we give back to the reservation.

Having done that, we're now headed into the second transaction with an
EFI and 180K of reservation.  Other threads apparently consumed all the
reservation for smaller transactions, such as timestamp updates.

Now let's say the first transaction gets written to disk and we crash
without ever completing the second transaction.  Now we remount the fs,
log recovery finds the unfinished EFI, and calls xfs_efi_recover to
finish the EFI.  However, xfs_efi_recover starts a new tr_itruncate
tranasction, which asks for 360K log reservation.  This is a lot more
than the 180K that we had reserved at the time of the crash.  If the
first EFI to be recovered is also pinning the tail of the log, we will
be unable to free any space in the log, and recovery livelocks.

Wengang confirmed this:

"Now we have the second transaction which has 180208 log bytes reserved
too. The second transaction is supposed to process intents including
extent freeing.  With my hacking patch, I blocked the extent freeing 5
hours. So in that 5 hours, 180208 (NOT 360416) log bytes are reserved.

"With my test case, other transactions (update timestamps) then happen.
As my hacking patch pins the journal tail, those timestamp-updating
transactions finally use up (almost) all the left available log space
(in memory in on disk).  And finally the on disk (and in memory)
available log space goes down near to 180208 bytes.  Those 180208 bytes
are reserved by [the] second (extent-free) transaction [in the chain]."

Wengang and I noticed that EFI recovery starts a transaction, completes
one step of the chain, and commits the transaction without completing
any other steps of the chain.  Those subsequent steps are completed by
xlog_finish_defer_ops, which allocates yet another transaction to
finish the rest of the chain.  That transaction gets the same tr_logres
as the head transaction, but with tr_logcount = 1 to force regranting
with every roll to avoid livelocks.

In other words, we already figured this out in commit 929b92f64048d
("xfs: xfs_defer_capture should absorb remaining transaction
reservation"), but should have applied that logic to each intent item's
recovery function.  For Wengang's case, the xfs_trans_alloc call in the
EFI recovery function should only be asking for a single transaction's
worth of log reservation -- 180K, not 360K.

Quoting Wengang again:

"With log recovery, during EFI recovery, we use tr_itruncate again to
reserve two transactions that needs 360416 log bytes.  Reserving 360416
bytes fails [stalls] because we now only have about 180208 available.

"Actually during the EFI recover, we only need one transaction to free
the extents just like the 2nd transaction at RUNTIME.  So it only needs
to reserve 180208 rather than 360416 bytes.  We have (a bit) more than
180208 available log bytes on disk, so [if we decrease the reservation
to 180K] the reservation goes and the recovery [finishes].  That is to
say: we can fix the log recover part to fix the issue. We can introduce
a new xfs_trans_res xfs_mount->tr_ext_free

{
  tr_logres = 175488,
  tr_logcount = 0,
  tr_logflags = 0,
}

"and use tr_ext_free instead of tr_itruncate in EFI recover."

However, I don't think it quite makes sense to create an entirely new
transaction reservation type to handle single-stepping during log
recovery.  Instead, we should copy the transaction reservation
information in the xfs_mount, change tr_logcount to 1, and pass that
into xfs_trans_alloc.  We know this won't risk changing the min log size
computation since we always ask for a fraction of the reservation for
all known transaction types.

This looks like it's been lurking in the codebase since commit
3d3c8b5222b92, which changed the xfs_trans_reserve call in
xlog_recover_process_efi to use the tr_logcount in tr_itruncate.
That changed the EFI recovery transaction from making a
non-XFS_TRANS_PERM_LOG_RES request for one transaction's worth of log
space to a XFS_TRANS_PERM_LOG_RES request for two transactions worth.

Fixes: 3d3c8b5222b92 ("xfs: refactor xfs_trans_reserve() interface")
Complements: 929b92f64048d ("xfs: xfs_defer_capture should absorb remaining transaction reservation")
Suggested-by: Wengang Wang <wen.gang.wang@oracle.com>
Cc: Srikanth C S <srikanth.c.s@oracle.com>
[djwong: apply the same transformation to all log intent recovery]
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>

---
## [arp242/toml](https://github.com/arp242/toml)@[4642c11e24...](https://github.com/arp242/toml/commit/4642c11e24ae6ae39490ba19b8fce6fc14afc101)
#### Saturday 2023-09-23 00:15:11 by Martin Tournoij

Change bare key characters to Letter and Digit

I believe this would greatly improve things and solves all the issues,
mostly. It's a bit more complex, but not overly so, and can be
implemented without a Unicode library without too much effort. It offers
a good middle ground, IMHO.

I don't think there are ANY perfect solutions here and that *anything*
will be a trade-off. That said, I do believe some trade-offs are better
than others, and after looking at a bunch of different options I believe
this is by far the best path for TOML.

Advantages:

- This is what I would consider the "minimal set" of characters we need
  to add for reasonable international support, meaning we can't really
  make a mistake with this by accidentally allowing too much.

  We can add new ranges in TOML 1.2 (or even change the entire approach,
  although I'd be very surprised if we need to), based on actual
  real-world feedback, but any approach we will take will need to
  include letters and digits from all scripts.

  This is a strong argument in favour of this and a huge improvement: we
  can't really do anything wrong here in a way that we can't correct
  later. Being conservative for these type of things is is good!

- This solves the normalisation issues, since combining characters are
  no longer allowed in bare keys, so it becomes a moot point.

  For quoted keys normalisation is mostly a non-issue because few people
  use them and the specification even strongly discourages people from
  using them, which is why this gone largely unnoticed and undiscussed
  before the "Unicode in bare keys" PR was merged.[1]

- It's consistent in what we allow: no "this character is allowed, but
  this very similar other thing isn't, what gives?!"

  Note that #954 was NOT about "I want all emojis to work" per se, but
  "this character works fine, but this very similar doesn't". This shows
  up in a number of things aside from emojis:

      a.toml:
              Input:   ; = 42  # U+037E GREEK QUESTION MARK (Other_Punctuation)
              Error:   line 1: expected '.' or '=', but got ';' instead

      b.toml:
              Input:   · = 42  # # U+0387 GREEK ANO TELEIA (Other_Punctuation)
              Error:   (none)

      c.toml:
              Input:   – = 42  # U+2013 EN DASH (Dash_Punctuation)
              Error:   line 1: expected '.' or '=', but got '–' instead

      d.toml:
              Input:   ⁻ = 42  # U+207B SUPERSCRIPT MINUS (Math_Symbol)
              Error:   (none)

      e.toml:
              Input:   ＃x = "commented ... or is it?"  # # U+FF03 FULLWIDTH NUMBER SIGN (Other_Punctuation)
              Error:   (none)

  "Some punctuation is allowed but some isn't" is hard to explain, and
  also not what the specification says: "Punctuation, spaces, arrows,
  box drawing and private use characters are not allowed." In reality, a
  lot of punctuation IS allowed, but not all.

  People don't read specifications, nor should they. People try
  something and sees if it works. Now it seems to work on first
  approximation, and then (possibly months later) it seems to "break".

  It should either allow everything or nothing. This in-between is just
  horrible. From the user's perspective this seems like a bug in the
  TOML parser, but it's not: it's a bug in the specification.

  There is no good way to communicate this other than "these codepoints,
  which cover most of what you'd write in a sentence, except when it
  doesn't".

  In contrast, "we allow letters and digits" is simple to spec, simple
  to communicate, and should have a minimum potential for confusion. The
  current spec disallows some things seemingly almost arbitrary while
  allowing other very similar characters.

- This avoids a long list of confusable special TOML characters; some
  were mentioned above but there are many more:

      '＃' U+FF03     FULLWIDTH NUMBER SIGN (Other_Punctuation)
      '＂' U+FF02     FULLWIDTH QUOTATION MARK (Other_Punctuation)
      '﹟' U+FE5F     SMALL NUMBER SIGN (Other_Punctuation)
      '﹦' U+FE66     SMALL EQUALS SIGN (Math_Symbol)
      '﹐' U+FE50     SMALL COMMA (Other_Punctuation)
      '︲' U+FE32     PRESENTATION FORM FOR VERTICAL EN DASH (Dash_Punctuation)
      '˝'  U+02DD     DOUBLE ACUTE ACCENT (Modifier_Symbol)
      '՚'  U+055A     ARMENIAN APOSTROPHE (Other_Punctuation)
      '܂'  U+0702     SYRIAC SUBLINEAR FULL STOP (Other_Punctuation)
      'ᱹ'  U+1C79     OL CHIKI GAAHLAA TTUDDAAG (Modifier_Letter)
      '₌'  U+208C     SUBSCRIPT EQUALS SIGN (Math_Symbol)
      '⹀'  U+2E40     DOUBLE HYPHEN (Dash_Punctuation)
      '࠰'  U+0830     SAMARITAN PUNCTUATION NEQUDAA (Other_Punctuation)

  Is this a big problem? I guess it depends; I can certainly imagine an
  Armenian speaker accidentally leaving an Armenian apostrophe.

- Maps to identifiers in more (though not all) languages. We discussed
  whether TOML keys are "strings" or "identifiers" last week in #966 and
  while views differ (mostly because they're both) it seems to me that
  making it map *closer* is better. This is a minor issue, but it's
  nice.

That does not mean it's perfect; as I mentioned all solutions come with
a trade-off. The ones made here are:

- The biggest issue by far is that the check to see if a character is
  valid may become more complex for some languages and environments that
  can't rely on a Unicode database being present.

  However, implementing this check is trivial logic-wise: it just needs
  to loop over every character and check if it's in a range table. You
  already need this with TOML 1.0, it's just that the range tables
  become larger.

  The downside is it needs a somewhat large-ish "allowed characters"
  table with 716 start/stop ranges, which is not ideal, but entirely
  doable and easily auto-generated. It's ~164 lines hard-wrapped at
  column 80 (or ~111 lines hard-wrapped at col 120). tomlc99 is 2,387
  lines, so that seems within the limits of reason (actually, reading
  through the tomlc99 code adding multibyte support at all will be the
  harder part, with this range table being a minor part).

- There's a new Unicode version roughly every year or so, and the way
  it's written now means it's "locked" to Unicode 9 or, optionally, a
  later version. This is probably fine: Apple's APFS filesystem (which
  does normalisation) is "locked" to Unicode 9.0; HFS+ was Unicode 3.2.
  Go is Unicode 8.0. etc. I don't think this is really much of an issue
  in practice.

  I choose Unicode 9 as everyone supports this; I doubted a long time
  over it, and we can also use a more recent version. I feel this gives
  us a nice balance between reasonable interoperability while also
  future-proofing things.

- ABNF doesn't support Unicode. This is a tooling issue, and in my
  opinion the tooling should adjust to how we want TOML to look like,
  rather than adjusting TOML to what tooling supports. AFAIK no one uses
  the ABNF directly in code, and it's merely "informational".

  I'm not happy with this, but personally I think this should be a
  non-issue when considering what to do here. We're not the only people
  running in to this limitation, and is really something that IETF
  should address in a new RFC or something ("Extra Augmented BNF"?)

Another solution I tried is restricting the code ranges; I twice tried
to do this (with some months in-between) and spent a long time looking
at Unicode blocks and ranges, and I found this impractical: we'll end up
with a long list which isn't all that different from what this proposal
adds.

Fixes #954
Fixes #966
Fixes #979
Ref #687
Ref #891
Ref #941

---

[1]:
Aside: I encountered this just the other day as I created a TOML file
with all UK election results since 1945, which looks like:

     [1950]
     Labour       = [13_266_176, 315, 617]
     Conservative = [12_492_404, 298, 619]
     Liberal      = [ 2_621_487,   9, 475]
     Sinn_Fein    = [    23_362,   0,   2]

That should be Sinn_Féin, but "Sinn_Féin" seemed ugly, so I just wrote
it as Sinn_Fein. This is what most people seem to do.

---
## [Mu-L/NetHack](https://github.com/Mu-L/NetHack)@[1a64ee1c28...](https://github.com/Mu-L/NetHack/commit/1a64ee1c285f8d9a27e58efa3989a281413f9b8e)
#### Saturday 2023-09-23 00:19:52 by PatR

github PR #259 - paranoid_confirmation:trap

Fairly old pull request from copperwater:  add new paranoid_confirm
setting 'trap'.

The old commit suffered from bit rot and merging needed too much
fixing up despite there not being many bands of change in the commit's
diffs.  I ultimately redid it from scratch, although the two biggest
chunks of code started with copy+paste of the pull request's commit.

It operates like paranoid:pray.  Setting paranoid:trap adds a new
"Really step into <trap>?" y/n prompt when attempting to move
into/onto a known trap, even if an object covers it on the map.
Setting both 'paranoid:Confirm trap' turns that into a yes/no prompt.
(Adding 'Confirm' affects other paranoid confirmations; in addition
to requiring yes<return> rather than just y to accept, it also forces
no<return> to reject.)

However, moving into a known trap that is considered to be harmless
behaves as if no trap was present.  Some of the trap classification
might be out of date; several types of traps have undergone changes
since implementation of the original pull request, notably anti-magic
field.  When the hero is hallucinating, all known traps are considered
harmful since the map no longer reliably describes them.

Preceding a movement command with the 'm' prefix also behaves as if
no trap was present, bypassing confirmation for that move, similar to
how paranoid:swim currently behaves.  Being stunned or confused also
behaves as if no trap was present, taking priority over hallucination.

This updates the documentation.

Supersedes #259
Closes #259

---
## [arp242/toml](https://github.com/arp242/toml)@[d369334fd4...](https://github.com/arp242/toml/commit/d369334fd4e967f5ee786a8ef922a182445ecf3c)
#### Saturday 2023-09-23 00:39:50 by Martin Tournoij

Change bare key characters to Letter and Digit

I believe this would greatly improve things and solves all the issues,
mostly. It's a bit more complex, but not overly so, and can be
implemented without a Unicode library without too much effort. It offers
a good middle ground, IMHO.

I don't think there are ANY perfect solutions here and that *anything*
will be a trade-off. That said, I do believe some trade-offs are better
than others, and I've made it no secret that I feel the current
trade-off is a bad one. After looking at a bunch of different options I
believe this is by far the best path for TOML.

Advantages:

- This is what I would consider the "minimal set" of characters we need
  to add for reasonable international support, meaning we can't really
  make a mistake with this by accidentally allowing too much.

  We can add new ranges in TOML 1.2 (or even change the entire approach,
  although I'd be very surprised if we need to), based on actual
  real-world feedback, but any approach we will take will need to
  include letters and digits from all scripts.

  This is a strong argument in favour of this and a huge improvement: we
  can't really do anything wrong here in a way that we can't correct
  later, unlike what we have now, which is "well I think it probably
  won't cause any problems, based on what these 5 European/American guys
  think, but if it does: we won't be able to correct it".

  Being conservative for these type of things is good!

- This solves the normalisation issues, since combining characters are
  no longer allowed in bare keys, so it becomes a moot point.

  For quoted keys normalisation is mostly a non-issue because few people
  use them, which is why this gone largely unnoticed and undiscussed
  before the "Unicode in bare keys" PR was merged.[1]

- It's consistent in what we allow: no "this character is allowed, but
  this very similar other thing isn't, what gives?!"

  Note that #954 was NOT about "I want all emojis to work" per se, but
  "this character works fine, but this very similar doesn't". This shows
  up in a number of things aside from emojis:

      a.toml:
              Input:   ; = 42  # U+037E GREEK QUESTION MARK (Other_Punctuation)
              Error:   line 1: expected '.' or '=', but got ';' instead

      b.toml:
              Input:   · = 42  # # U+0387 GREEK ANO TELEIA (Other_Punctuation)
              Error:   (none)

      c.toml:
              Input:   – = 42  # U+2013 EN DASH (Dash_Punctuation)
              Error:   line 1: expected '.' or '=', but got '–' instead

      d.toml:
              Input:   ⁻ = 42  # U+207B SUPERSCRIPT MINUS (Math_Symbol)
              Error:   (none)

      e.toml:
              Input:   ＃x = "commented ... or is it?"  # U+FF03 FULLWIDTH NUMBER SIGN (Other_Punctuation)
              Error:   (none)

  "Some punctuation is allowed but some isn't" is hard to explain, and
  also not what the specification says: "Punctuation, spaces, arrows,
  box drawing and private use characters are not allowed." In reality, a
  lot of punctuation IS allowed, but not all (especially outside of the
  Latin character range by the way, which shows the Euro/US bias in how
  it's written).

  People don't read specifications in great detail, nor should they.
  People try something and sees if it works. Now it seems to work on
  first approximation, and then (possibly months or years later) it
  seems to "suddenly break". From the user's perspective this seems like
  a bug in the TOML parser, but it's not: it's a bug in the
  specification. It should either allow everything or nothing. This
  in-between is confusing and horrible.

  There is no good way to communicate this other than "these codepoints,
  which cover most of what you'd write in a sentence, except when it
  doesn't".

  In contrast, "we allow letters and digits" is simple to spec, simple
  to communicate, and should have a minimum potential for confusion. The
  current spec disallows some things seemingly almost arbitrary while
  allowing other very similar characters.

- This avoids a long list of confusable special TOML characters; some
  were mentioned above but there are many more:

      '＃' U+FF03     FULLWIDTH NUMBER SIGN (Other_Punctuation)
      '＂' U+FF02     FULLWIDTH QUOTATION MARK (Other_Punctuation)
      '﹟' U+FE5F     SMALL NUMBER SIGN (Other_Punctuation)
      '﹦' U+FE66     SMALL EQUALS SIGN (Math_Symbol)
      '﹐' U+FE50     SMALL COMMA (Other_Punctuation)
      '︲' U+FE32     PRESENTATION FORM FOR VERTICAL EN DASH (Dash_Punctuation)
      '˝'  U+02DD     DOUBLE ACUTE ACCENT (Modifier_Symbol)
      '՚'  U+055A     ARMENIAN APOSTROPHE (Other_Punctuation)
      '܂'  U+0702     SYRIAC SUBLINEAR FULL STOP (Other_Punctuation)
      'ᱹ'  U+1C79     OL CHIKI GAAHLAA TTUDDAAG (Modifier_Letter)
      '₌'  U+208C     SUBSCRIPT EQUALS SIGN (Math_Symbol)
      '⹀'  U+2E40     DOUBLE HYPHEN (Dash_Punctuation)
      '࠰'  U+0830     SAMARITAN PUNCTUATION NEQUDAA (Other_Punctuation)

  Is this a big problem? I guess it depends; I can certainly imagine an
  Armenian speaker accidentally leaving an Armenian apostrophe.

  Confusables is also an issue with different scripts (Latin and
  Cyrillic is well-known), but this is less of an issue since it's not
  syntax, and also something that's fundamentally unavoidable in any
  multi-script environment.

- Maps closer to identifiers in more (though not all) languages. We
  discussed whether TOML keys are "strings" or "identifiers" last week
  in #966 and while views differ (mostly because they're both) it seems
  to me that making it map *closer* is better. This is a minor issue,
  but it's nice.

That does not mean it's perfect; as I mentioned all solutions come with
a trade-off. The ones made here are:

- The biggest issue by far is that the check to see if a character is
  valid may become more complex for some languages and environments that
  can't rely on a Unicode database being present.

  However, implementing this check is trivial logic-wise: it just needs
  to loop over every character and check if it's in a range table. You
  already need this with TOML 1.0, it's just that the range tables
  become larger.

  The downside is it needs a somewhat large-ish "allowed characters"
  table with 716 start/stop ranges, which is not ideal, but entirely
  doable and easily auto-generated. It's ~164 lines hard-wrapped at
  column 80 (or ~111 lines hard-wrapped at col 120). tomlc99 is 2,387
  lines, so that seems within the limits of reason (actually, reading
  through the tomlc99 code adding multibyte support at all will be the
  harder part, with this range table being a minor part).

- There's a new Unicode version roughly every year or so, and the way
  it's written now means it's "locked" to Unicode 9 or, optionally, a
  later version. This is probably fine: Apple's APFS filesystem (which
  does normalisation) is "locked" to Unicode 9.0; HFS+ was Unicode 3.2.
  Go is Unicode 8.0. etc. I don't think this is really much of an issue
  in practice.

  I choose Unicode 9 as everyone supports this; I doubted a long time
  over it, and we can also use a more recent version. I feel this gives
  us a nice balance between reasonable interoperability while also
  future-proofing things.

- ABNF doesn't support Unicode. This is a tooling issue, and in my
  opinion the tooling should adjust to how we want TOML to look like,
  rather than adjusting TOML to what tooling supports. AFAIK no one uses
  the ABNF directly in code, and it's merely "informational".

  I'm not happy with this, but personally I think this should be a
  non-issue when considering what to do here. We're not the only people
  running in to this limitation, and is really something that IETF
  should address in a new RFC or something ("Extra Augmented BNF"?)

Another solution I tried is restricting the code ranges; I twice tried
to do this (with some months in-between) and spent a long time looking
at Unicode blocks and ranges, and I found this impractical: we'll end up
with a long list which isn't all that different from what this proposal
adds.

Fixes #954
Fixes #966
Fixes #979
Ref #687
Ref #891
Ref #941

---

[1]:
Aside: I encountered this just the other day as I created a TOML file
with all UK election results since 1945, which looks like:

     [1950]
     Labour       = [13_266_176, 315, 617]
     Conservative = [12_492_404, 298, 619]
     Liberal      = [ 2_621_487,   9, 475]
     Sinn_Fein    = [    23_362,   0,   2]

That should be Sinn_Féin, but "Sinn_Féin" seemed ugly, so I just wrote
it as Sinn_Fein. This is what most people seem to do.

---
## [mnmaita/bevy](https://github.com/mnmaita/bevy)@[3ee9edf280...](https://github.com/mnmaita/bevy/commit/3ee9edf280c530f35a51049ec92fcfa552998614)
#### Saturday 2023-09-23 01:46:56 by Ethereumdegen

add try_insert to entity commands (#9844)

# Objective

- I spoke with some users in the ECS channel of bevy discord today and
they suggested that I implement a fallible form of .insert for
components.

- In my opinion, it would be nice to have a fallible .insert like
.try_insert (or to just make insert be fallible!) because it was causing
a lot of panics in my game. In my game, I am spawning terrain chunks and
despawning them in the Update loop. However, this was causing bevy_xpbd
to panic because it was trying to .insert some physics components on my
chunks and a race condition meant that its check to see if the entity
exists would pass but then the next execution step it would not exist
and would do an .insert and then panic. This means that there is no way
to avoid a panic with conditionals.

Luckily, bevy_xpbd does not care about inserting these components if the
entity is being deleted and so if there were a .try_insert, like this PR
provides it could use that instead in order to NOT panic.

( My interim solution for my own game has been to run the entity despawn
events in the Last schedule but really this is just a hack and I should
not be expected to manage the scheduling of despawns like this - it
should just be easy and simple. IF it just so happened that bevy_xpbd
ran .inserts in the Last schedule also, this would be an untenable soln
overall )

## Solution

- Describe the solution used to achieve the objective above.

Add a new command named TryInsert (entitycommands.try_insert) which
functions exactly like .insert except if the entity does not exist it
will not panic. Instead, it will log to info. This way, crates that are
attaching components in ways which they do not mind that the entity no
longer exists can just use try_insert instead of insert.

---

## Changelog

 

## Additional Thoughts

In my opinion, NOT panicing should really be the default and having an
.insert that does panic should be the odd edgecase but removing the
panic! from .insert seems a bit above my paygrade -- although i would
love to see it. My other thought is it would be good for .insert to
return an Option AND not panic but it seems it uses an event bus right
now so that seems to be impossible w the current architecture.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[dd6f51d9b6...](https://github.com/Paxilmaniac/Skyrat-tg/commit/dd6f51d9b6b970ec16d1398fe12516c039385263)
#### Saturday 2023-09-23 02:34:29 by SkyratBot

[MIRROR] Supermatter Delamination Balance Changes (Real) [MDB IGNORE] (#23670)

* Supermatter Delamination Balance Changes (Real) (#77996)

## About The Pull Request

lord forgive me I fucked up the merge conflict

The supermatter delamination countdown timer (how long it takes to go
boom-boom after hitting 0 integrity) has been lowered from 30 seconds to
13 seconds.
Removing a sliver from the supermatter, the traitor objective, will
further lower that down to 3 seconds.
Changes the wording on the mood effects from the supermatter
delaminating slightly.
The crystal uses SPAN_COMMAND on its final countdown, which means it
talk bigger.

## Why It's Good For The Game

Currently I feel that the supermatter delamination countdown overstays
its welcome. Ideally it provides tension to get the hell out, or perhaps
to make a risky last second play to try and save the supermatter.
However right now its at 30 seconds, which gives no danger of staying in
engineering right up to integrity 0, and keeps the tension at a high
note for too long, almost to the point of awkwardness. 13 seconds is a
good balance between get-the-fuck-out while still giving some leeway for
engineers to escape and crewmembers to jump in lockers, and feels quick
enough to give that danger that the supermatter should provide.
Additionally, removing a sliver from the supermatter lowers the cooldown
to 3 seconds. Right now this is one of the harder tasks a traitor can be
tasked with, while giving relatively little payoff sabatoge-wise. To the
point where I have seen engineers just let the traitor do it, as the
debuff it gives to the supermatter is minor. Now it makes the
supermatter delaminate almost immediately after hitting 0 integrity,
which means it will likely catch some engineers in the blast if a
traitor did it stealthy. This also makes it more risky to try and fix a
delamination if the engineering/security team did not stop the sliver
from being removed. All meaning succeeding at this task should be more
rewarding and damaging.
Finally the mood descriptions for the mood effects you get when a
supermatter delaminates have been changed. Currently they are pretty
gamey, and represent what the player might be thinking more than their
character. Additionally they were not very descriptive of where they
came from, which could be confusing.

## Changelog

:cl: Seven
balance: The supermatter delamination countdown has been lowered from 30
to 13 seconds
balance: Removing a sliver from the supermatter further lowers that down
to 3 seconds
balance: The supermatter crystal uses bigger text on its final countdown
spellcheck: Some supermatter delamination related mood descriptions have
been edited to explain the mood effect better
/:cl:

---------

Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>

* Supermatter Delamination Balance Changes (Real)

* Update scram.dm

---------

Co-authored-by: Lufferly <40921881+Lufferly@users.noreply.github.com>
Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[ed10226825...](https://github.com/CoiledLamb/lorbstation/commit/ed10226825bbef4e605d7e831ebb1d8f30f805f4)
#### Saturday 2023-09-23 02:55:51 by Jacquerel

Desouls Hivelord (#78213)

## About The Pull Request


![dreammaker_RJz4brjobM](https://github.com/tgstation/tgstation/assets/7483112/e5e4a3e9-ea6b-47f9-887c-3339d24d3fa8)

Replaces the sprite of the hivelord with a new one, in my continuing
quest to annihilate the old asteroid mob sprites.
A (never completed) asteroid mob resprite was actually my first PR, this
one is my 200th.
I am also planning on fucking with basic mob versions of these mobs some
time but the sprites can be atomised out.

In addition to replacing the old-ass MSPaint sprites, this PR also adds
a short death animation effect to the hivelord brood (from hivelords or
legions) which looks nicer than them just vanishing instantly upon
death.

Look at this video for an example of the animation:
https://www.youtube.com/watch?v=cKaskN5-y2A

## Why It's Good For The Game

Looks nicer.

## Changelog

:cl:
image: Hivelords have a new sprite.
image: Hivelord and Legion brood have a death animation.
/:cl:

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[009af8c2ce...](https://github.com/CoiledLamb/lorbstation/commit/009af8c2ce5c18ca4fdaceb4e4d2c17d8e8d6d00)
#### Saturday 2023-09-23 02:55:51 by nikothedude

[TEST-MERGE FIRST] Wound refactor number two: Full synthetic support (#78124)

## About The Pull Request

Heavily refactors wounds AGAIN.

The primary thing this PR does is completely change how wounds are
generated and added - while the normal "hit a guy til they bleed" stuff
works about the same, asking for a specific type of wound, say, like how
vending machines try to apply a compound fracture sometimes, isnt going
to work if we ever get any non-organic wounds, which the previous
refactor allowed.

With this PR, however...
* You can now ask for a specific type of wound via
get_corresponding_wound_type(), which takes wound types, a limb, wound
series, etc. and will try to give you a wound fitting those
specifications - but also, a wound that can be applied to a limb.
* This will allow for a vending machine to apply a compound fracture to
a human, but a collapsed superstructure (assuming my synth wounds go in)
to a robot

There are now new "series types" and "wound specific types" that allow
us to designate what series are "mainline" and randomly generatable, and
what are "alternate types" and must be generated manually - you can see
the documentation in wounds.dm.

The behavior of limping and interaction delays has been abstracted to
datum/wound from bone wounds to allow just, general ease of development

Pregen data now allows for series-specific wound penalties. Example: You
could set a burn wound's series wound penalty to 40, which would make
wound progression in the burn category easier - but it would not make it
any easier to get a slashing wound. As it stands wound penalties are for
wounds globally

Scar files are now picked in a "priority" list, where the wound checks
to see if the limb has a biostate before moving down in said list.
Example: Wounds will check for flesh first, if it finds it - it will use
the flesh scar list. Failing that, they then check bone - if it uses
that, it will use the bone scar list. This allows for significantly more
modular scars that dont even need much proc editing when a new wound
type is added

Misc changes: most initial() usage has been replaced by singleton
datums, wound_type is now wound_types and thus wounds can accept
multiple wound types, wounds can now accept multiple tool behaviors for
treatment, wounds now have a picking weight so we can make certain
wounds rarer flatly,

This PR also allows for wounds to override lower severity wounds on
generation, allowing eswords to jump to avulsions - but in spirit of
refactoring, this has been disabled by default (see pregen data's
competition_mode var).
## Why It's Good For The Game

Code quality is good!

Also, all the changes above allow wounds to be a MUCH more modular
system, which is one of its biggest problems right now - everything is
kinda hardcoded and static, making creative work within wounds harder to
do.

## Changelog
:cl:
refactor: Refactored wounds yet again
fix: Wounds are now picked from the most severe down again, meaning
eswords can jump to avulsions
fix: Scar descs are now properly applied
/:cl:

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[25b1203a97...](https://github.com/TheVekter/tgstation/commit/25b1203a971ab7091abbe75cacfce1ba28b62a78)
#### Saturday 2023-09-23 03:10:15 by Jacquerel

You can do revival surgery on Ian (#78288)

## About The Pull Request

Allows you to perform revival surgery on any mob which is organic or
looks humanoid.
This means yes: Corgis, Goliaths, ~~Syndicate mobs~~ not those because
they spawn human corpses and delete themselves.
No: Slimes, Ghosts, General Beepsky.

Splits revival surgery into a subtype used for "mobs" and a subtype for
"mobs with brains" as the former don't have any brains to damage.

Additionally by special request, Ian can now wear an eyepatch and will
automatically put one on if he is brought back from death.

![image](https://github.com/tgstation/tgstation/assets/7483112/eff91bf6-4f80-4d8b-9062-1a5d4af85d39)

## Why It's Good For The Game

Currently you revive dead pets either by creating a magical reagent out
of holy water or by buying a mining item which also brainwashes them,
however reasonably our skilled medical team should be able to put a dog
back together and now can.
When you fuck up one of the stages of Tend Wounds on a kitten and stab
it to death with your scalpel, now you can fix it.
Expands the possibilities of vetinerary roleplay.

## Changelog

:cl:
add: Many kinds of mobs can now be brought back to life through revival
surgery.
add: Dogs can wear eyepatches.
/:cl:

---
## [SylvKT/SylvKT.github.io](https://github.com/SylvKT/SylvKT.github.io)@[06522e95e8...](https://github.com/SylvKT/SylvKT.github.io/commit/06522e95e859dd567153b9bbb13ea717ca3d4a64)
#### Saturday 2023-09-23 03:16:16 by SylvKT

remove shitty fucking arial i fucking hate arial fuck arial

---
## [BillyONeal/vcpkg-tool](https://github.com/BillyONeal/vcpkg-tool)@[21bb63300b...](https://github.com/BillyONeal/vcpkg-tool/commit/21bb63300bf39c89315cb54526c5aa05e0f48861)
#### Saturday 2023-09-23 03:16:22 by Billy Robert O'Neal III

Substantially overhaul how x-ci-verify-versions works:

* Print error messages naming the file we're complaining about so that IDEs etc. can go to the file, (Using the standard path: kind: message format)
* Record the location in try_load_port and friends instead of requiring callers recover that themselves.
* Make load_git_versions_file return the expected path of the versions file so that callers need not recover that themselves.
* Delete registry_location from SourceControlFileAndLocation because it is not ever set. (I don't mind this member existing if there's data to go there but right now, there is not).
* Deduplicate 'try vcpkg.json, also try CONTROL' behavior from x-add-version and x-ci-verify-versions.
* Don't stop validating versions information at the first error.

The remaining places that are still thinking about adding / "vcpkg.json" are now only:

* format-manifest when deciding the new path after parsing a CONTROL
* new when deciding the new path
* inside try_load_port and friends themselves
* the horrible mess that is how vcpkgpaths loads the consumer-manifest

---
## [nevimer/Bubberstation](https://github.com/nevimer/Bubberstation)@[c6e0ba7516...](https://github.com/nevimer/Bubberstation/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Saturday 2023-09-23 03:27:42 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [SKCro/WebTV-HD](https://github.com/SKCro/WebTV-HD)@[315c62745b...](https://github.com/SKCro/WebTV-HD/commit/315c62745b946a1b7799c6bec7b3934d8482f75c)
#### Saturday 2023-09-23 04:21:27 by SK

Adding radio button styles! (Kinda)

yeah the positioning is shit, I'll fix that eventually™

---
## [Drillur/LORED](https://github.com/Drillur/LORED)@[90392ae69e...](https://github.com/Drillur/LORED/commit/90392ae69ebb3733a4da4e35e119eb5ca52fd46a)
#### Saturday 2023-09-23 04:34:31 by Drillur

Game is very smooth until the final added Wish

Tomorrow, I will resume adding Wishes. The pacing of the game seems good, everything seems pretty bug-free... oops, after I wrote that, I remembered something was wrong. I just can't remember what was wrong. I didn't write it down :(

There seems to be something funny going on with the Price Progress Bar in tooltips. I will keep an eye on that and make it perfect.

Saving and Loading is actually working perfectly----oops! Actually, SOMETIMES--not every time--when loading, a random wish's Rewards will not get loaded. So it would then be beneficial to deny the wish to get a fresh one. dunno why it doesn't happen EVERY time, but i'll find out why i guess

---
## [warsaids/Shiptest-DonDIgrad](https://github.com/warsaids/Shiptest-DonDIgrad)@[b22529fc74...](https://github.com/warsaids/Shiptest-DonDIgrad/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Saturday 2023-09-23 04:48:44 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [mintme-com/core-geth](https://github.com/mintme-com/core-geth)@[5161c8d924...](https://github.com/mintme-com/core-geth/commit/5161c8d924803f941c75585b77b43e41bf240f39)
#### Saturday 2023-09-23 05:06:23 by meows

contracts/checkpointoracle,contracts/checkpointoracle/contract,params/types/genesisT: run 'go generate ./...' with partial success

A few things I learned along the way this evening.

- solc in path must be 0.6.0 or some mysterious upper
bound less than the latest available versions that I
also tried.
- solcjs is not solc. npm install solc installs solcjs
which is like solc but is not solc.

All of this partially fixes an error which looked like this.

go generate ./...
protoc-gen-go: no such flag -import_path
--go_out: protoc-gen-go: Plugin failed with status code 1.
accounts/usbwallet/trezor/trezor.go:45: running 'protoc': exit status 1
Error: Source file requires different compiler version (current compiler is 0.8.5+commit.a4f2e591.Linux.g++) - note that nightly builds are considered to be strictly less than the released version
 --> contract/oracle.sol:1:1:
    |
           1 | pragma solidity ^0.6.0;
         | ^^^^^^^^^^^^^^^^^^^^^^^

              contracts/checkpointoracle/oracle.go:20: running 'solc': exit status 1

The error now looks like this

go generate ./...
protoc-gen-go: no such flag -import_path
--go_out: protoc-gen-go: Plugin failed with status code 1.

Maybe we don't even want these changes. I don't know.
I just want the command to work for the sake of order
in the universe.

But seriously
- maybe we should upgrade the Solidity version pragma too/instead?
- maybe proto-gen-go actually wants a different version than 'latest',
  (which is what 'make devtools' installs).
- maybe we report the issue at ethereum. their trezor.go looks same
  same.

Goodnight, to dream of green lights.

Date: 2022-12-20 19:40:04-08:00
Signed-off-by: meows <b5c6@protonmail.com>

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[51c82f3222...](https://github.com/Derpguy3/tgstation/commit/51c82f32223179f7263dd8d4de11eb62f23ef8fd)
#### Saturday 2023-09-23 05:10:32 by RICK IM RI

Adds Blood-drunk and demonic frost miner boss music. (#78123)

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

---
## [JaredEllis/GameJamF23](https://github.com/JaredEllis/GameJamF23)@[784b3fd6d4...](https://github.com/JaredEllis/GameJamF23/commit/784b3fd6d4af8b0c26a9ba51524c600ee43d1379)
#### Saturday 2023-09-23 05:57:34 by Jared Ellis

Merge pull request #3 from JaredEllis/ai

holy fucking shit we got AI now

---
## [RalfJung/rust](https://github.com/RalfJung/rust)@[3de0f19c41...](https://github.com/RalfJung/rust/commit/3de0f19c41cbfc5901e5fbd4c107e263d9f1a359)
#### Saturday 2023-09-23 05:57:53 by bors

Auto merge of #11437 - y21:issue-11422, r=xFrednet

[`implied_bounds_in_impls`]: don't ICE on default generic parameter and move to nursery

Fixes #11422

This fixes two ICEs ([1](https://github.com/rust-lang/rust-clippy/issues/11422#issue-1872351763), [2](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=2901e6febb479d3bd2a74f8a5b8a9305)), and moves it to nursery for now, because this lint needs some improvements in its suggestion (see #11435, for one such example).

changelog: Moved [`implied_bounds_in_impls`] to nursery (Now allow-by-default)
[#11437](https://github.com/rust-lang/rust-clippy/pull/11437)
changelog: [`implied_bounds_in_impls`]: don't ICE on default generic parameter in supertrait clause

r? `@xFrednet` (since you reviewed my PR that added this lint, I figured it might make sense to have you review this as well since you have seen this code before. If you don't want to review this, sorry! Feel free to reroll then)

--------

As for the ICE, it's pretty complicated and very confusing imo, so I'm going to try to explain the idea here (partly for myself, too, because I've confused myself several times writing- and fixing this):
<details>
<summary>Expand</summary>

The general idea behind the lint is that, if we have this function:
```rs
fn f() -> impl PartialEq<i32> + PartialOrd<i32> { 0 }
```
We want to lint the `PartialEq` bound because it's unnecessary. That exact bound is already specified in `PartialOrd<i32>`'s supertrait clause:
```rs
trait PartialOrd<Rhs>: PartialEq<Rhs> {}
//    PartialOrd<i32>: PartialEq<i32>
```

 The way it does this is in two steps:
- Go through all of the bounds in the `impl Trait` return type and collect each of the trait's supertrait bounds into a vec. We also store the generic arguments for later.
  - `PartialEq` has no supertraits, nothing to add.
  - `PartialOrd` is defined as `trait PartialOrd: PartialEq`, so add `PartialEq` to the list, as well as the generic argument(s) `<i32>`

Once we are done, we have these entries in the vec: `[(PartialEq, [i32])]`

- Go through all the bounds again, and looking for those bounds that have their trait `DefId` in the implied bounds vec.
  - `PartialEq` is in that vec. However, that is not enough, because the trait is generic. If the user wrote `impl PartialEq<String> + PartialOrd<i32>`, then `PartialOrd` clearly doesn't imply `PartialEq`. Which means, we also need to check that the generic parameters match. This is why we also collected the generic arguments in `PartialOrd<i32>`. This process of checking generic arguments is pretty complicated and is also where the two ICEs happened.

The way it checks that the generic arguments match is by comparing the generic parameters in the super trait clause:
```rs
trait PartialOrd<Rhs>: PartialEq<Rhs> {}
//                     ^^^^^^^^^^^^^^
```
...this needs to match...
```rs
fn f() -> impl PartialEq<i32> + ...
//             ^^^^^^^^^^^^^^
```
In the compiler, the `Rhs` generic parameter is its own type and we cannot just compare it to `i32`. We need to "substitute" it.
Internally, `Rhs` is represented as `Rhs#1` (the number next to # represents the type parameter index. They start at 0, but 0 is "reserved" for the implicit `Self` generic parameter).

How do we go from `Rhs#1` to `i32`? Well, we know that all the generic parameters had to be substituted in the `impl ... + PartialOrd<i32>` type. So we subtract 1 from the type parameter index, giving us 0 (`Self` is not specified in that list of arguments). We use that as the index into the generic argument list `<i32>`. That's `i32`. Now we know that the supertrait clause looks like `: PartialEq<i32>`.

Then, we can compare that to what the user actually wrote on the bound that we think is being implied: `impl PartialEq<i32> + ...`.

Now to the actual bug: this whole logic doesn't take into account *default* generic parameters. Actually, `PartialOrd` is defined like this:
```rs
trait PartialOrd<Rhs = Self>: PartialEq<Rhs> {}
```
If we now have a function like this:
```rs
fn f() -> impl PartialOrd + PartialEq {}
```
that logic breaks apart... We look at the supertrait predicate `: PartialEq<Rhs>` (`Rhs` is `Rhs#1`), then take the first argument in the generic argument list `PartialEq<..>` to resolve the `Rhs`, but at this point we crash because there *is no* generic argument.
The index 0 is out of bounds. If this happens (and we even get to linting here, which could only happen if it passes typeck), it must mean that that generic parameter has a default type that is not required to be specified.

This PR changes the logic such that if we have a type parameter index that is out of bounds, it looks at the definition of the trait and check that there exists a default type that we can use instead.
So, we see `<Rhs = Self>`, and use `Self` for substitution, and end up with this predicate: `: PartialEq<Self>`. No crash this time.

</details>

---
## [Regisle/PathOfBuilding](https://github.com/Regisle/PathOfBuilding)@[fb66ee7051...](https://github.com/Regisle/PathOfBuilding/commit/fb66ee70516cdb416b6f9c7799307c5757e199b2)
#### Saturday 2023-09-23 06:53:10 by LocalIdentity

Fix accuracy of skill Mana/Life cost calculations (#6220)

* Rough code to male it work

* Recommit changes

* Fix breakdowns

* Correct values for Divine Blessing

* Fix breakdown when using Lifetap or Blood Magic

* Fix display of skills with innate Life Cost

---------

Co-authored-by: LocalIdentity <localidentity2@gmail.com>

---
## [zartashaasif/zartashaasif](https://github.com/zartashaasif/zartashaasif)@[8aa26c69e3...](https://github.com/zartashaasif/zartashaasif/commit/8aa26c69e387be4d21f3d53193c82da7a8dec362)
#### Saturday 2023-09-23 07:01:55 by zartasha asif

Update README.md

I am a Bachelor of IT and a self-taught Front-End Web Developer from Pakistan with a passion for creating exceptional user experiences. My diverse skill set includes expertise in HTML, CSS, JavaScript, React.js, Bootstrap, and Tailwind, which I use to craft functional and intuitive web interfaces. I would be delighted to hear from you if you are looking for a collaborative partner to bring your unique vision to life. Let's work together to build something amazing! 💻🚀
Click to expand for more details 🤭

    Previous Experience: I have been a JavaScript and React.js developer at the Code Lab and IT Solution Software House.
    Projects: I have worked on various web development projects, creating responsive and user-friendly interfaces.
    Education: I hold a Master degree in Information Technology from The  university of sarghoda.

---
## [ProjectFaerun/Faerun](https://github.com/ProjectFaerun/Faerun)@[10250fdf8d...](https://github.com/ProjectFaerun/Faerun/commit/10250fdf8d2fd880f6dd4236b2bc6b4ae45e5bc0)
#### Saturday 2023-09-23 09:28:10 by neutrondecay

More tweaks

* Kingdom of Elturgard breaks up properly when Zariel takes Elturel
* Female Grand Dukes get their title
* Aylin loses her nickname at the right time, and get her girlfriend back

---
## [fgnm/libgdx](https://github.com/fgnm/libgdx)@[e1d1fdc5fb...](https://github.com/fgnm/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Saturday 2023-09-23 10:23:44 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[1be0841d98...](https://github.com/Mothblocks/tgstation/commit/1be0841d98f215a0e94245c33317232bafa59342)
#### Saturday 2023-09-23 10:58:26 by Time-Green

Removes COMSIG_AREA_INITIALIZED_IN (#78143)

Literally just me stealing #77207 completely muhahahhahahah screw you
@Mothblocks
I did add some documentation and some radnebula related cleaning and
testing to make it work well

Copied from original PR:

> Please do NOT add code to InitAtom, it is extremely hot. The
conditions on this alone were costing nearly 200ms on my extremely
powerful machine.
> 
> Changes the radioactive nebula to perform its work by looping over
every space tile on init (which on my machine is faster than the time
being wasted on this signal), and adds a subsystem that does this in
SS_BACKGROUND every 30 seconds (usually completeable in about half a
second) for any new atoms, because the effect is hardly noticeable
anyway with how green space is.

Honestly we really don't care that much about stuff being initialized in
space. Everything that walks into space (about everything that matters
to players), is completely unaffected by this change, but roundstart is
now slightly faster

---
## [Updated-NoCheatPlus/NoCheatPlus](https://github.com/Updated-NoCheatPlus/NoCheatPlus)@[4817eed02e...](https://github.com/Updated-NoCheatPlus/NoCheatPlus/commit/4817eed02e99117db83a552b0b2a3979ef072d21)
#### Saturday 2023-09-23 11:16:35 by Lysandr0

Minor refactor for moving checks, rename Folia class, integrate Gutenberg as an ordinary check.

Move hard-coded magic into its own package (envelope); move checks.moving.magic class to the moving utilities package; split envelopes methods into its own class (PlayerEnvelopes); BounceUtil -> BounceHandler and to the envelope class; BounceType -> to the checks.moving.model package.

* Renamed Folia class to "SchedulerHelper" (name is up to debate, feel free to add)

* Gutenberg won't check for availability anymore. The event was introduced in 1.5 and NCP doesn't support versions lower than that anymore.

* Move "honeyBlockSidewayCollision" method to PlayerEnvelopes.

* Fix compilation errors in RichBoundsLocation and get rid of unused method.

* Get rid of the "split move" flag: too internal of an option and should never be disabled anyway.

* Clarify docs

* LiftOffEnvelope:
-Get rid of min/max jump distinction.
-Decrease normal jump height down to 1.26.

* SurvivalFly: various adjustments... Key change are:
 -The riddance of vAcc. Useless with the upcoming vDistRel rework;
-Unbind to the horizontal-push-speed mechanic from hard-coded magic. (Please Asofold for the love God why did you not document this kind of stuff... Why was it needed);
-Merge vDistWeb, vDistLevitation, vDistBush into vDistRel, climbables and powder snow are still handled in their respective methods because we are restricted by NCP's current  infrastructure and we cannot predict those two (powder snow in particular)
-Move honeyBlock collision to richboundslocation.

* RichEntityLocation:
-Force legacy players to have vines attached to a solid block to climb up.
-Check for client version for fullHeight setting as well.
-Move liquid pushing stuff to RuchEntityLocation

---
## [BananaDroid-Lab/frameworks_base](https://github.com/BananaDroid-Lab/frameworks_base)@[b1e6168de6...](https://github.com/BananaDroid-Lab/frameworks_base/commit/b1e6168de664792b02b8fd9f2c6e0489da2461ff)
#### Saturday 2023-09-23 11:46:38 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[60855885de...](https://github.com/diphons/D8G_Kernel_oxygen/commit/60855885de7b2a727e230fb7b041cd1e7d4da018)
#### Saturday 2023-09-23 12:19:35 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [piotrsiupa/karnaugh-solver](https://github.com/piotrsiupa/karnaugh-solver)@[68e8ef02e7...](https://github.com/piotrsiupa/karnaugh-solver/commit/68e8ef02e72cd4d420f2761367be02e8f62c034f)
#### Saturday 2023-09-23 12:28:04 by Piotr Siupa

Optimizing via brute force instead of a heuristic

This is not entirely finished but it took a lot of time and I need a
backup before continuing.
I'm not even sure if this is an NP problem. It kinda looks similar to NP
but I have trouble finding an example for which a heuristic gives worse
result. (Maybe it because more complicated examples can be run only with
use of heuristic to not take ridiculously long time so I don't have a
comparison.) I'm gonna need to research that more thoroughly.

---
## [warpspin/smallweb](https://github.com/warpspin/smallweb)@[4be4b78e5b...](https://github.com/warpspin/smallweb/commit/4be4b78e5be3af5ffef591a389c3ac94fa6e6fc7)
#### Saturday 2023-09-23 12:58:54 by Andy

Add https://www.cerealously.net/feed

A wonderful website authored by an a single individual (Dan) about news and reviews in the world of American breakfast cereals. The writing is genuinely lovely, and clearly a product of personal passion.

Note that this is NOT a link affiliate/marketing spam blog for cereals. The author has no direct relation to any cereal companies (at least to my best knowledge), and the writing is clearly the author's direct, personal feelings about the subject matter.

Highly recommend for the small web :)

---
## [anuprasadkulkarni/conditional_statement](https://github.com/anuprasadkulkarni/conditional_statement)@[7203ca332b...](https://github.com/anuprasadkulkarni/conditional_statement/commit/7203ca332b7b6025710278fde80e551accd04631)
#### Saturday 2023-09-23 13:08:24 by anuprasadkulkarni

Add files via upload


Conditional Statements
Please write Python Programs for all the problems .
1.	 Take a variable ‘age’ which is of positive value and check the following:
a.	If age is less than 10, print “Children”.
b.	If age is more than 60 , print ‘senior citizens’
c.	 If it is in between 10 and 60, print ‘normal citizen’

2.	Find  the final train ticket price with the following conditions. 
a.	If male and sr.citizen, 70% of fare is applicable
b.	If female and sr.citizen, 50% of fare is applicable.
c.	If female and normal citizen, 70% of fare is applicable
d.	If male and normal citizen, 100% of fare is applicable
[Hint: First check for the gender, then calculate the fare based on age factor.. For both Male and Female ,consider them as sr.citizens if their age >=60]
3.	Check whether the given number is positive and divisible by 5 or not.  

Conditional Statements
Please implement Python coding for all the problems.

1.	A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exist in list1.
B) How do we create a sequence of numbers in Python?
C)  Read the input from keyboard and print a sequence of numbers up to that number

2.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
 Create a dictionary such that list2 are keys and list 1 are values..

3.	 Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is an odd number in the list1..

       4.     Write a simple user defined function that greets a person in such a way that :
             i) It should accept both the name of the person and message you want to deliver.
              ii) If no message is provided, it should greet a default message ‘How are you’
           Ex: Hello ---xxxx---, How are you  -🡪 default message.
            Ex: Hello ---xxxx---, --xx your message xx---

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[433764f1b0...](https://github.com/treckstar/yolo-octo-hipster/commit/433764f1b05c744dd0de550a9db488ae3399d6fc)
#### Saturday 2023-09-23 14:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[4b73b37d60...](https://github.com/mc-oofert/tgstation/commit/4b73b37d60dbff8746ffb3e1eb0f6ff51895fffc)
#### Saturday 2023-09-23 14:33:00 by jimmyl

Heretic Knock Path (#78108)

## About The Pull Request

other changes: GODMODEd mobs cannot receive embeds or bleed, admins can
now use the traitor panel to give heretics a focus

adds a new heretic path, the path of knock
its a path about opening shit and having access
wound opening included, and stealing
this is its award icon

![ascended](https://github.com/tgstation/tgstation/assets/70376633/01473bf2-5c44-4574-850c-83fb5db204fd)
its knowledge is as follows:

### A Locksmith’s Secret
starting knowledge, unlocks the key blade which also works as a crowbar


https://github.com/tgstation/tgstation/assets/70376633/3690232d-5687-4b0c-a9cc-b6374e7f1850

### Grasp of Knock
it literally just opens stuff (also makes a knocking sound)
unbolts bolted airlocks and opens them, opens locked closets, opens
mechas, logs you into consoles
(comms consoles are with barebones head-level access, no buying shuttle,
but hey you can shitpost over comms)
Sidepaths: Ashen Eyes, Codex Cicatrix


https://github.com/tgstation/tgstation/assets/70376633/8b890d69-ee03-4d12-99dd-dde7b4483cd4

### Key Keepers Burden
transmute a rod,wallet, and some id card to create an eldritch id card
(very original naming), the ID card used is not preserved
this ID card functions essentially as a superior agent card, using other
IDs on it makes it be consumed by the eldritch ID and have its accesses
and forms added into it, you can use it inhand to turn it into any of
the cards that were consumed
in addition you can hit two airlocks with it to link them together to
create portals under the doors, which has a green glow
going through the portal as a Heretic gets you to the other destination
going through as a nonheretic lands you in a random onstation airlock,
SM chamber included if youre unlucky
1 id card can only have 1 set of portals, making another destroys the
former set, one of the airlocks being destroyed also destroys them


https://github.com/tgstation/tgstation/assets/70376633/e96a518e-b35d-44aa-9a7c-8f2103feab6f

### Rite Of Passage
transmute a white crayon, a multitool, and a plank to create consecrated
lintel
heretics can use this cool looking book to create a 8 second shield that
knocks back any nonheretic that tries to pass
also its ranged


https://github.com/tgstation/tgstation/assets/70376633/036e0875-c422-433e-87b3-71328cb2bf8a

### Mark Of Knock
the mansus grasp will now mark its victim for like 10 seconds
marked victims are denied access by all objects, public airlocks
included


https://github.com/tgstation/tgstation/assets/70376633/6187ef36-30f4-4a92-af21-e5b288afb869

### Burglars Finesse
steal a random item from the victims backpack (or other storage item if
they dont have a backpack) and puts it into your hand
the victim will probably hear you and also gets a chat message about
this



https://github.com/tgstation/tgstation/assets/70376633/2529fa78-616d-4a46-ae18-3cb22efb1ab1

### Ritual of knowledge
this is nothing new i put this here to keep it in order

### Apetra Vulnera (sidepath with flesh)
the victim receives bleed wounds on every single bodypart that has more
than 15 brute
if they dont have a bodypart that has >= 15 brute they get a random
wound anyway so
side paths are: blood siphon and void cloak



https://github.com/tgstation/tgstation/assets/70376633/3c2cd21e-edbc-4956-8c2d-cd9a42b87f33

### Wave of Desperation (sidepath with flesh)
cannot be casted uncuffed with no bola, can be casted cuffed with no
bola, with a bola and no cuffs
adjacent mobs are knocked down, mobs are repulsed away, your cuffs and
bola are destroyed, and you gain a status effect that:
after 12 seconds makes you unconscious for 20 seconds
5 min cooldown


https://github.com/tgstation/tgstation/assets/70376633/da480921-d5dd-4b46-b2e8-0cf543640bf9

### Opening Blade
your blade has a 35% chance to cause a weeping avulsion on hit


https://github.com/tgstation/tgstation/assets/70376633/b6fd2837-6b0a-4a5a-bc7b-b9c3f7f715d1

### Caretakers Last Refuge
you can only cast this when not near sentient living beings
while in refuge you are invincible and near transparent, cannot use your
hands or spells
also immune to damage slowdown, being hit with a null rod cancels this
also if you lose your focus you get out of refuge


https://github.com/tgstation/tgstation/assets/70376633/f053cfd8-2a16-4195-8004-17df077983ca



https://github.com/tgstation/tgstation/assets/70376633/72330486-5273-4123-a108-b437b56120c4

### Many secrets behind the Spider Door (Ascension)
ritual needs 3 bodies without organs in their chest
when successfully performed you ascend and;
open a tear in reality (not the BoH one) which;
Polls all ghosts with sentient mob enabled to spawn and siege the
station, ghosts can interact with the portal to spawn as a random
eldritch mob
spawned mobs are loyal to whoever ascended and on examine can identify
their master
also fills the entire room with purple light

also the heretics opening blade is upgraded to a 65% chance, and they
gain Ascended Shapeshift which allows them to shapeshift into eldritch
mobs, and its not 1 choice only



https://github.com/tgstation/tgstation/assets/70376633/8d06286e-789d-442f-b33c-878d26deab07


## Why It's Good For The Game

its cool i think and an option for those wanting to steal and be sneaky
and stuff

## Changelog
:cl:
add: heretic knock path and its respective items and award
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [PeterAhiaba/Peters_Project](https://github.com/PeterAhiaba/Peters_Project)@[829429a985...](https://github.com/PeterAhiaba/Peters_Project/commit/829429a98586859aae649bff2851d776934eb3a8)
#### Saturday 2023-09-23 14:36:22 by PeterAhiaba

Add files via upload

This is a report on Students' Mental Health.
Data Source: Kaggle.com.

From this report, more female students struggle with mental health issues ranging from Depression, Anxiety, and Panic attacks, than their male counterparts.

83% of the female were dealing with mental health issues as against 16% of the male.

Of the 83% female, only 3.75% sought treatment, and of 16% male 0.26% sought treatment.

Of the 3.75% of females all were married except one and of the 0.2% of males who sought treatment all were married.

Deduction/Insight

1: Companionship and/or having a friend or family talk go a long way in the healing process for mental health issues.

2: Love is an antidote to mental health issues.

3: More attention should be given to the female child.

---
## [ejohnfel/FubarSel](https://github.com/ejohnfel/FubarSel)@[2583f4675e...](https://github.com/ejohnfel/FubarSel/commit/2583f4675e0d4d0210435dd1bbbfa6f683ad113c)
#### Saturday 2023-09-23 15:05:21 by Eric Johnfelt

Fucking Python PEP shit. sys.maxint removed for some dumb ass reason, causing exceptions in my code.

Fuckers claim there is no practical limit for ints as there are only practical limits on arrays. On any computer systems, MAX values for any numeric value is a fucking reality and should never be removed... fuckers!

Fixed with attempts = max_attempts + 1, assholes...

---
## [lnGoror/tgstation](https://github.com/lnGoror/tgstation)@[820c22a5f5...](https://github.com/lnGoror/tgstation/commit/820c22a5f5381364c595d21b6c047e269f7f0497)
#### Saturday 2023-09-23 15:17:00 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [lnGoror/tgstation](https://github.com/lnGoror/tgstation)@[63f7eb1a6a...](https://github.com/lnGoror/tgstation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Saturday 2023-09-23 15:17:00 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [openembedded/openembedded-core](https://github.com/openembedded/openembedded-core)@[909fd25c2e...](https://github.com/openembedded/openembedded-core/commit/909fd25c2ebd25f5d3bc560e26f9df6862e033d0)
#### Saturday 2023-09-23 15:25:50 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [yoctoproject/poky](https://github.com/yoctoproject/poky)@[4682ae38f2...](https://github.com/yoctoproject/poky/commit/4682ae38f285f59b68196289ece5802460805201)
#### Saturday 2023-09-23 15:27:33 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

(From OE-Core rev: 909fd25c2ebd25f5d3bc560e26f9df6862e033d0)

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [villetoimela/villetoimela-site-v2](https://github.com/villetoimela/villetoimela-site-v2)@[fc83cdd505...](https://github.com/villetoimela/villetoimela-site-v2/commit/fc83cdd505443eafe960cb7605e5904514470385)
#### Saturday 2023-09-23 15:27:35 by Ville Toimela

Finally fucking did it. I hate myself because i cannot just pass props as normal element id="" because ScrollSection broke. Now i had to do that with UseRef and that was weird to use. STILL I DID IT yeehaw. fuck that take too much time tho

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[ae41c46c50...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/ae41c46c50b59f8e9d83ac5d413784420af02f97)
#### Saturday 2023-09-23 15:55:11 by Time-Green

Only double HCR for impressive greentexts (#78383)

There were a few exploits with free antags that would double your score.
This happened to me once by accident, but anyone could essentially
guarantee a point doubling.

I've changed the whole thing to only work for:
- Traitor
- Changeling
- Heretic
- Blood brother
- Headrev
- Wizard (you could get this with die of fate)
- Obsessed
- Magic and gun survivalists
- Holding the greentext book (because a cripple fighting for their life
for the greentext just seems funny and is rare enough)

Notably, revolutionairies, cult converts and brainwashed now no longer
pay out. Cult is pointless since you can't greentext without gibbing
(trust me I tried) and revolutionairy takes no effort other than having
strong teammates and doing nothing. There are a lot of other antags this
excludes, but those are mostly midrounds and non-humans (which are by
default excluded)

:cl:
balance: Only traitor, changeling, heretic, blood brother, headrev,
wizard, obsessed, magic/gun survivalists and greentext book holders can
now double their hardcore random score
qol: Redtexting as antag with hardcore random score will pay you default
points, instead of none (normal survival rules)
fix: End report screen will properly report hardcore random survival in
case of station destruction
/:cl:

---
## [adamoia/fachionadam.com](https://github.com/adamoia/fachionadam.com)@[5f853e68c1...](https://github.com/adamoia/fachionadam.com/commit/5f853e68c17ee0aa691dbd8140fce1de946ab60c)
#### Saturday 2023-09-23 16:00:29 by adamoia

Add files via upload

At [Your Store Name], we redefine fashion by curating a collection that speaks volumes about elegance, comfort, and individuality. Our passion for clothing transcends trends; we are dedicated to offering you not just garments but an experience that empowers your unique sense of style.

Discover Unparalleled Style

Step into a world where every stitch tells a story. Our wide-ranging selection of clothing encompasses the latest fashion trends as well as timeless classics. From sophisticated formal wear to casual chic, we have something to suit every occasion and taste.

Quality that Matters

We believe that true beauty lies in the details. That's why we source our fabrics with the utmost care and attention, ensuring that each piece you find at [Your Store Name] is a testament to craftsmanship and quality. Our commitment to sustainability also means you can feel good about your fashion choices.

Personalized Service

At [Your Store Name], we know that shopping for clothing is a personal experience. Our dedicated team of fashion experts is here to assist you, offering personalized advice and recommendations. Whether you need help finding the perfect outfit or styling tips, we're always at your service.

Effortless Shopping

We understand the value of your time, which is why we've created a seamless online shopping experience. Browse our collections, make secure payments, and have your fashion finds delivered to your doorstep with ease. It's fashion at your fingertips.

Stay Connected

Be the first to know about our latest arrivals, exclusive offers, and fashion inspiration by joining our community. Follow us on social media and subscribe to our newsletter to stay in the loop.

At [Your Store Name], we believe that clothing is not just about covering the body; it's about expressing your identity, boosting confidence, and embracing the art of self-expression. Join us in celebrating the beauty of fashion, and let us help you create your signature style.

Elevate your wardrobe today with adam fachion - Where Fashion Becomes You.

Feel free to customize this text to match your store's unique identity and brand philosophy. It's important to convey your store's values and what sets you apart from the competition.

---
## [Vincent983/tgstation](https://github.com/Vincent983/tgstation)@[a321623971...](https://github.com/Vincent983/tgstation/commit/a321623971250cc9e0abee5377cffef2de784b4e)
#### Saturday 2023-09-23 16:06:44 by ArcaneMusic

Conveyor Belts are now easier to extend and have screentips (#78278)

## About The Pull Request

Conveyor belt **stacks** now have a better examine text.

Using a conveyor belt stack on a placed conveyor belt now extends the
conveyor belt by 1 tile, linking to it's ID automatically, and makes for
much easier building of conveyor belt setups.

Conveyor belts now come jam packed with screentips.

I've also added the default tile place sound to the usage of conveyor
stacks to provide a tiny bit of audio feedback when placing new conveyor
belts.

## Why It's Good For The Game

Conveyor belts are just mind-numbingly annoying to use in a regular
round, and trying to set up a new conveyor belt setup is confusing if
you don't have ultra specific information about how to make one before
you even start. Hell, I remember I had to add the *real* construction
steps to the wiki like 6 years ago and I STILL hear people getting
confused about how these works.

This improves their ease of use, while also making everyone sleep a
little easier for those of us who use them.

## Changelog

:cl:
qol: Conveyor belts now have screentips and a better examine tip to
teach you how to set one up properly.
qol: Using a conveyor belt stack on a placed conveyor belt will extend
the conveyor belt to the output of that conveyor belt.. You can use this
to place fully integrated conveyor belts much easier now.
/:cl:

---
## [vbousquet/pinmame](https://github.com/vbousquet/pinmame)@[a37fbbe90f...](https://github.com/vbousquet/pinmame/commit/a37fbbe90f79865b4d1f48228b9f2acc925a9be3)
#### Saturday 2023-09-23 17:05:52 by toxie

address issue #102

cite from mjr:

The change to this file in commit 9ed410d, which is labeled as ported from MAME/MESS, adds a new bug, which affects DCS playback quality.

The changes are all to the implementation of the ABS (ABSOLUTE VALUE) instruction. The old version had an explicit CLR_S to clear the AS flag in ASTAT, whereas the new code deletes the CLR_S and substitutes CLR_FLAGS.

The addition of CLR_FLAGS is correct, since the instruction is documented as updating the AC-AN-AV-AZ flags. But the deletion of CLR_S is a bug, because the documentation also says that ABS must set or clear AS, according to the sign of the source operand. (See the ADSP 2100 User's Manual, 3rd edition, September 1995, section 15, ABSOLUTE VALUE (ABS) instruction: "AS: Set if the source operand is negative. Cleared otherwise.") CLR_FLAGS doesn't affect AS, so if AS was set going into the instruction, it'll still be set coming out, even if the operand was positive.

This isn't just a harmless bookkeeping detail - it actually breaks the DCS games in a subtle way! You can observe the effect of the bug on the DCS games by firing up ST-TNG LX7, going to the test menu, running the sound test, and letting track 1 ("1ST TUNE") run on auto-repeat. You'll hear a sort of flatulent distortion, which is occurring because that new ABS instruction bug is randomizing about 30% of the DCS frames decoded. It's actually affecting all of the tracks, but it seems to be more audible in tracks with lots of low bass frequencies, and just causes some annoying popping and crackling on most of the other tracks.

If anyone has been asking why the audio for all of the DCS games has been sucking lately, this is probably the answer.

Solution: Add back the CLR_S that was there before, right after the new CLR_FLAGS.

---
## [SkyN9ne/WindowsTerminal](https://github.com/SkyN9ne/WindowsTerminal)@[21464fe41c...](https://github.com/SkyN9ne/WindowsTerminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Saturday 2023-09-23 17:33:06 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [lavillastrangiato/lvs-aurora](https://github.com/lavillastrangiato/lvs-aurora)@[652a3d02d4...](https://github.com/lavillastrangiato/lvs-aurora/commit/652a3d02d4260aea7f34c64814f409a677b063a0)
#### Saturday 2023-09-23 17:42:27 by Wowzewow (Wezzy)

Adds Storage Container Animations (#17329)

* Much ado about the Bagginses

* god i hate manually mapped shit

* Update code/game/objects/items/weapons/storage/storage.dm

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>

* fixes

* yes

* Update code/game/objects/items/weapons/storage/bags.dm

Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---------

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>
Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---
## [LukePavelka/sbox-stargate](https://github.com/LukePavelka/sbox-stargate)@[93f12b42db...](https://github.com/LukePavelka/sbox-stargate/commit/93f12b42db8e9fb022826dcdaed0221ecbbb7f59)
#### Saturday 2023-09-23 18:14:25 by Patrik Šimanský

Fix DHD hardlocking the gate

Damn this was fucking awful to track down

---
## [nptnc/HourSocket](https://github.com/nptnc/HourSocket)@[aa69a0771c...](https://github.com/nptnc/HourSocket/commit/aa69a0771c6212501beb5300cbb33853c9b40c94)
#### Saturday 2023-09-23 18:16:41 by PeeblyWeeb

fuck you nptnc, i dont know what you did but i had to resolve merge conflicts.

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[f373f05075...](https://github.com/carlarctg/tgstation/commit/f373f0507570506470f73d65d105d978e4e7ab8f)
#### Saturday 2023-09-23 20:30:55 by Hatterhat

buffs embed pulling with hemostats, allows wirecutters to pull embeds too (#78256)

## About The Pull Request
- Wirecutters or tools with wirecutter behaviors are now valid for
plucking embeds.
- Pluck speed no longer **starts** at 2.5 seconds, which is a pretty
dang long time, especially if you have bad embed RNG. I'll do the math
and run some more tests in the morning.
- Wirecutters have a speed malus in regards to plucking embeds. I should
probably make it worse to account for, like, jaws of life or something.
- Plucking embeds with wirecutters now hurts! It hurts way less than
ripping it out with your hands, but it still hurts!

For comparison's sake, bare-handed throwing star removal compared to
possible tools.

![image](https://github.com/tgstation/tgstation/assets/31829017/96730fa5-77b8-4f31-83ba-48d36e4e419b)


## Why It's Good For The Game
Embeds kinda suck to deal with. This is intentional - I get that.

However, hemostat pulling is kind of... kind of bad. Awful, really. 2.5
seconds is a lot of time. I know it's not supposed to be the best
option, but if you've got a tool, I'd at least like to think it'd be
slightly less bad than shoving your fingers into your wound?

## Changelog

:cl:
balance: Pulling embedded items e.g. shrapnel with hemostats is now a
lot faster, and scales appropriately with toolspeed.
balance: You can now pull embedded items with wirecutters, at a speed
penalty.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [cmoore53/CSC-425-Taskmaster](https://github.com/cmoore53/CSC-425-Taskmaster)@[446b058212...](https://github.com/cmoore53/CSC-425-Taskmaster/commit/446b0582128b025cb65f9211f7c860a757b01ef3)
#### Saturday 2023-09-23 20:43:38 by cmoore53

TaskList now takes properties

Pain.
In more detail, you can now pass an array of data for tasks into TaskList, and TaskList will pass each spot in the array to Task, and then you'll get a bunch of tasks back in your page. There was an annoying bug with tasks though, where you have to type tasks.tasks.(whatever) because for some reason the code passes tasks, which contains the object tasks, which contains the array. I hate JavaScript.

---
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[9dbf819e8a...](https://github.com/Zonespace27/cmss13/commit/9dbf819e8a0512809c54ae8aae43749265a939bf)
#### Saturday 2023-09-23 20:55:12 by forest2001

Codebook Optimisation (#4393)

# About the pull request
For as long as we've had a codebook it's been a pain in the arse to
read/synchronise from a staff POV. With this, codebooks will all share
the same codes per-faction.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Makes events that use codebooks actually viable.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: Codebooks are now faction based rather than individually unique.
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[a8edd9004f...](https://github.com/effigy-se/effigy-se/commit/a8edd9004f1875bd3be409e2f382933a74bf8a40)
#### Saturday 2023-09-23 22:02:46 by carlarctg

Gun kits don't need cable coil or tools, halved crafting time (#78419)

## About The Pull Request

Crafting R&D guns from gun kits no longer requires tools or cable coil.
The decloner and energy crossbow still need reagents.

Halved R&D gun crafting time. 20->10 seconds.

## Why It's Good For The Game

These changes were made a long, long while ago and honestly while I
understand gun kits I don't understand why it was made So. Annoying. To
make the fucking guns once you got everything ready. It makes it a total
annoyance. You spent 40 minutes getting all the tech for it, you
shouldn't have to also get tools and cables and wait 20 seconds standing
still.

Anyone who has played ingame like any time after that change can attest
how underused any R&D gun is now. X-ray laser guns still DESTROY blobs
but people don't even THINK about them because of the dumb annoying
recipe (alongside RnD being a pain now).

Simply put this just. Makes life easier for security officers. And
reduces tool dependency.

## Changelog

:cl:
qol: Crafting R&D guns from gun kits no longer requires tools or cable
coil. The decloner and energy crossbow still need reagents.
qol: Halved R&D gun crafting time. 20->10 seconds.
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[68b6c1fa75...](https://github.com/effigy-se/effigy-se/commit/68b6c1fa753a4ae33cbe2d2a603041db4abdc7cf)
#### Saturday 2023-09-23 22:02:46 by RikuTheKiller

Rounded supermatter delamination times to 5 seconds, restored old mood messages (#78335)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Makes the supermatter delaminate in 15 seconds instead of 13 and 5
seconds instead of 3 if a sliver has been taken from it, mainly to
please perfectionists (me and some others who commented on the PR) as
well as giving people at least a chance to escape delam round removal.

I don't like it when flavorful text is replaced by bland and
not-as-funny alternatives.
Also, how the hell is it gamey for staff to know the engineers are in
charge of the power?
It's honestly more gamey for them to know what a resonance cascade or
supermatter delamination is, so I'd say you've done the opposite of what
the goal was with the message changes on top of making them less fun in
general. I disapprove.

Oh, yeah, and the SM now reports the times correctly due to it reporting
them every 5 seconds, meaning people would only see the 10 second
announcement. Now there is going to be a 15 second announcement as well.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Watering down messages to be bland is just, like, less fun, ya know?
I didn't see a single person in support of the message changes apart
from the PR author, everyone else was just complaining about them,
including myself.

Also, several people mentioned the fact it could just be 15 instead of
13 for a nice round number, including myself. I also made the sliver
delamination time 5 seconds instead of 3 seconds because you pretty much
can't get out in time, especially if the game is laggy. 3 - 5 people
being round removed because of one traitor objective with no chance to
escape it is just bad gameplay.

Oh, and, bugfix good, I suppose.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
balance: Supermatter now takes 15 seconds to delaminate normally and 5
if a sliver has been taken from it. Gives a little more time to escape
in the case of the sliver and also evens out the times to please
perfectionists.
fix: Supermatter now accurately reports it's detonation time.
spellcheck: Supermatter mood descriptions have been reverted back to
their old, more flavorful selves.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [xPokee/tgstation](https://github.com/xPokee/tgstation)@[4792a8e19d...](https://github.com/xPokee/tgstation/commit/4792a8e19dc6885a2f6e8d25f1086505624e7a6c)
#### Saturday 2023-09-23 22:10:47 by carlarctg

Nerfs Confusion symptom for diseases (#77991)

## About The Pull Request

Removed the threshold for confusion symptom that adds illiteracy to the
disease.

Clamps confusion symptom's confusion to a maximum of 30 seconds.

Confusion as a debuff no longer guarantees random movement if you're
resting.

## Why It's Good For The Game

> Removed the threshold for confusion symptom that adds illiteracy to
the disease.

This virus makes you unable to actually treat yourself when cured, which
is frankly bonkers. Viruses are too virulent and it's rare that a doctor
actually gets to a biosuit in time to inoculate themselves, and if they
forget internals they're screwed anyways. People should be able to fix
their own got damn disease, this is asinine.

> Clamps confusion symptom's confusion to a maximum of 30 seconds.

The lack of clamping literally makes this symptom send your confusion
level to the fucking atmosphere, you can easily get upwards of 5 minutes
of confusion left because it doesn't clamp, adds 16 seconds per
activation, which is made even worse by the fact that confusion gets
stronger the more duration confusion has on you.

> Confusion as a debuff no longer guarantees random movement if you're
resting.

This remedies the last bit by not making it a literal guarantee that you
can't move in any direction after...... *3* triggers of confusion. It
should be obvious to anyone how absurd this is.

Honestly, it's plain as day that the only reason any of this ended up
like it is because of poor coding and oversights. This is just bringing
things down to their designed level.

## Changelog

:cl:
del: Removed the threshold for confusion symptom that adds illiteracy to
the disease.
balance: Clamps confusion symptom's confusion to a maximum of 30
seconds.
qol: Confusion as a debuff no longer guarantees random movement if
you're resting.
/:cl:

---
## [xPokee/tgstation](https://github.com/xPokee/tgstation)@[a5aef3b823...](https://github.com/xPokee/tgstation/commit/a5aef3b823dd3b8b5bfe40d68bbc0f89b403f79a)
#### Saturday 2023-09-23 22:10:47 by MrMelbert

Replaces Ascended Blade Heretic stun imminuty with a stun absorption effect (it's not as cool as it sounds)  (#78060)

## About The Pull Request

Instead of being completely immune to stuns after ascension, blade
heretics now have a stun absorption. This is the effect that His Grace
and the Bastard Sword use.

It functions similarly, in that it stops you from being hardstunned, but
the difference it is they are only immune to a limited amount of stuns
for a limited amount of time before it recharges.

Currently that number is 45 seconds of stuns, with a 2 minute recharge,
meaning if you take more than 45 seconds of stun effects you will stop
being immune.

Bear in mind this still provides full immunity to being stamcrit*, as
stam doesn't contribute towards "seconds stunned" number.

*Unless you used all 45 seconds of stun immunity then you will no longer
be immune until you recharge.

Also to compensate, I gave them a slightly modifier protecting against
knockdowns.

## Why It's Good For The Game

I forgot Stun Absorptions were a thing entirely when making this even
though I refactored the darn things.

Anyways, the reason why I'm doing this is that Stun Absorptions are just
a slightly more fair, less overt way of providing stun immunity, and I
think it fits the theme more.

You're supposed to be a master duelist, but being able to take on a
dozen people at once is not entirely intended (even though this is the
ascension, I know). Stun Absorptions lend better to that, since you run
out of stun juice eventually before you have to pull back.

Though ultimately this doesn't change very much, as we use very few
hardstuns now-a-days:

- A flashbang will contribute about 10 seconds of stun time
- A flash is similar to a flashbang
- Bodythrows and tackles are less than 5 seconds
- Beepsky, 10 seconds
- Stamcrit, 0 seconds, but you are still slowed by stamina damage
- A banana peel, default is roughly 6 seconds. <-- (This is why I gave
them a knockdown modifier)

However it does mean you can't really tank an AI stun turret all day.
That's Rust's thing. Go play Rust Heretic.

## Changelog

:cl: Melbert
balance: Ascended Blade Heretics no longer have blanket stun immunity,
they now have 45 seconds of stun absorption that recharges after 2
minutes - think His Grace. This doesn't affect stamcrit (still immune to
that) (assuming you haven't consumed all of your immunity charge) but
does affect hard CC such as slips, flashbangs, or beepsky.
balance: Ascended Blade Heretics now have a 0.75 modifier to incoming
knockdowns.
/:cl:

---
## [cacko/gonic](https://github.com/cacko/gonic)@[8095379451...](https://github.com/cacko/gonic/commit/8095379451243d4a8bb4a4c69b6e575a30cb28f6)
#### Saturday 2023-09-23 22:29:17 by cacko

Another commit to keep my CAN streak going.

I don't know what the hell I was thinking.

workaround for ant being a pile of fail

magic, have no clue but it works

I had a cup of tea and now it's fixed

well crap.

hey, what's that over there?!

freemasonry

debug suff

Rush B!

and so the crazy refactoring process sees the sunlight after some months in the dark!

freemasonry

Herp derp I left the debug in there and forgot to reset errors.

add actual words

hey, look over there!

DNS_PROBE_FINISHED_NXDOMAIN

We've known each other for so long

add dirty scripts from the dark side of the universe

more ignores

diaaaaaazeeeeeeeeeepam

remove debug
all good

Your commit is writing checks your merge can't cash.

---
## [staten-island-tech/flexbox-gallery-project-squoosh4](https://github.com/staten-island-tech/flexbox-gallery-project-squoosh4)@[39dbd8e0f8...](https://github.com/staten-island-tech/flexbox-gallery-project-squoosh4/commit/39dbd8e0f8383d77a31d2a04308a277610ef2df4)
#### Saturday 2023-09-23 23:09:11 by Tritical1

god must either really hate me or is trying to make me objectively the goat

he cant let me have any fucking breathing me room he just like my parents fr

---

