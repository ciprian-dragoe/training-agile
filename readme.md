Create a new sprint board from this template [link](https://quire.io/w/ERP_TEMPLATE/12/As_a_User_I_want_to_list_all_the_products_a_use...?sublist=ERP&view=board)

Git flow:
1. Before creating a new branch choose which is the source branch
   1. `git checkout master`
   1. If you get an error it most probably is caused that you have uncommited files on the current branch (`git status`)
1. Name the new branch following the pattern ID_short_description_of_ticket
   1. `git checkout -b 1_delete_transaction`
1. Write your code and then commit it
   1. `git add .`
   1. `git commit -m "meaningful commit message about you have modified"`
1. Push your code to github
   1. `git push origin 1_delete_transaction` (supposed our branch name is 1_delete_transaction)
1. On GitHub create a new Pull Request
   1. Press the `Pull requests button`
   1. Press the `New pull request button`
   1. Press the `compare` button and select then name of your branch you pushed at the previous step
   1. Press the `base` button and select the `master` branch
   1. Press the `Create pull request` button
