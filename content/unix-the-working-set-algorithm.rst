Unix : the  "working set" algorithm
###################################
:date: 2010-12-04 23:04
:author: ankur
:category: Tech
:tags: Unix
:slug: unix-the-working-set-algorithm

I took my end semester exam today on the design of the\ `Unix operating
system`_. Most of it was a breeze. However, before the exam, a little
confusion cropped up regarding the `"working set" algorithm`_ in "`on
demand paging`_\ ". I had initially thought that it was just a regular
`LRU`_ implementation, but it apparently isn't. I've looked around the
internet and I can not really find any details on the implementation. If
you know a resource, please do drop in the link as a comment?

I'll take a brief example to show the difference between the two
implementations, one being a regular LRU, and the other being the
variant which is what is apparently actually used.

Consider this **stream of requests** : 24, 15, 18, 23, 24, 17, 18, 17,
17, 15, 24, 17, 24, 18 and assume a **window size** of **4**.

.. raw:: html

   <table style="text-align:center">

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

Page reference

.. raw:: html

   </th>

.. raw:: html

   <th>

Simple LRU

.. raw:: html

   </th>

.. raw:: html

   <th>

Variant

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td style="text-align:center">

24

.. raw:: html

   </td>

.. raw:: html

   <td style="text-align:center">

24

.. raw:: html

   </td>

.. raw:: html

   <td style="text-align:center">

24

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

15

.. raw:: html

   </td>

.. raw:: html

   <td>

24,15

.. raw:: html

   </td>

.. raw:: html

   <td>

24,15

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

18

.. raw:: html

   </td>

.. raw:: html

   <td>

24,15,18

.. raw:: html

   </td>

.. raw:: html

   <td>

24,15,18

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

23

.. raw:: html

   </td>

.. raw:: html

   <td>

24,15,18,23

.. raw:: html

   </td>

.. raw:: html

   <td>

24,15,18,23

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

24

.. raw:: html

   </td>

.. raw:: html

   <td>

15,18,23,24

.. raw:: html

   </td>

.. raw:: html

   <td>

15,18,23,24

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

17

.. raw:: html

   </td>

.. raw:: html

   <td>

18,23,24,17

.. raw:: html

   </td>

.. raw:: html

   <td>

18,23,24,17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

18

.. raw:: html

   </td>

.. raw:: html

   <td>

23,24,17,18

.. raw:: html

   </td>

.. raw:: html

   <td>

23,24,17,18

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

17

.. raw:: html

   </td>

.. raw:: html

   <td>

23,24,18,17

.. raw:: html

   </td>

.. raw:: html

   <td>

24,18,17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

17

.. raw:: html

   </td>

.. raw:: html

   <td>

23,24,18,17

.. raw:: html

   </td>

.. raw:: html

   <td>

18,17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

15

.. raw:: html

   </td>

.. raw:: html

   <td>

24,18,17,15

.. raw:: html

   </td>

.. raw:: html

   <td>

18,17,15

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

24

.. raw:: html

   </td>

.. raw:: html

   <td>

18,17,15,24

.. raw:: html

   </td>

.. raw:: html

   <td>

17,15,24

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

17

.. raw:: html

   </td>

.. raw:: html

   <td>

18,15,24,17

.. raw:: html

   </td>

.. raw:: html

   <td>

15,24,17

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

24

.. raw:: html

   </td>

.. raw:: html

   <td>

18,15,17,24

.. raw:: html

   </td>

.. raw:: html

   <td>

15,17,24

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

18

.. raw:: html

   </td>

.. raw:: html

   <td>

15,17,24,18

.. raw:: html

   </td>

.. raw:: html

   <td>

17,24,18

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

I have marked the beginning of variation in red. So, which one is
correct?? I used the variant in the test because that's what our
lecturer had said was right.

.. _Unix operating system: http://en.wikipedia.org/wiki/Unix
.. _"working set" algorithm: http://en.wikipedia.org/wiki/Working_set
.. _on demand paging: http://en.wikipedia.org/wiki/Demand_paging
.. _LRU: http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used
