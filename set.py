#demonstate the set 
pcb={"Biology","Zoology","Botany","Crop science","Dairy",
     "Fishery","English",
     "Hindi"}

pcm={"Physics","Chemistry","Maths","Electromics","English"}

print(pcb,"\n")
print(pcm,'\n')

#methods of set @1.add,2.update,3.pop(),4.clear(),
#5.remove(),6.discard , 7.intersection,8.difference,9.union,10.copy()

#@1
print("\n ***************Adding Items*************** \n ")
print("before Adding Item : ",pcm)
pcm.add("calculas")
print("After Adding Item:",pcm)

#@2
print("\n ***************Updating Items***************")
print("\n before Updating Items: ",pcm)
math_sylabus={"limit","Continuty","Diffrentiation",'Integration',"Vector",
              "Deravatives","Deravatives"}
pcm.update(math_sylabus)
print("\n After Updating Item :",pcm)


#@3
print("\n ***************Deleting  Items*************** \n ")
print("\n This Item Deleted From The Set :: = ",pcm.pop())

#@4
print("\n before deleting Item : \n",pcm)
#pcm.remove("Deravatives")
print("\n before Adding Item : \n",pcm)

#@5
print("\n before Discarding  an  Item \n: ",pcm)
pcm.discard("Application Of Deravatives") #this method don't show any error
print("\n After Discarding  an  Item \n: ",pcm)
pcm.discard("Vectors")


#@6
print("\n ***************Intersecting Items*************** \n ")
pcb={"Biology","Zoology","Botany","Crop science","Dairy",
     "Fishery","English",
     "Hindi"}

pcm={"Physics","Chemistry","Maths","Electromics","English","Hindi"}
print("\n before The Intersection \n: ",pcm)
common_sub=pcm.intersection(pcb)
print("\n After  The Intersection \n: ",common_sub)

#@7
print("\n *************** Item Difference *************** \n ")
print("\n before The Difference \n: ",pcm)
diff=pcm.difference(pcb)
print("\n After  The Difference \n: ",diff)

#@8
print("\n *************** Items Union *************** \n ")
print("\n before The union \n: ",pcm)
all_sub=pcm.union(pcb)
print("\n After  The Union \n: ",all_sub)

#@9
print("\n *************** Items Copy *************** \n ")
science=all_sub.copy()
print("\n \t Copeid Set = ",science)

#@10
print("\n *************** Clearing All Items *************** \n ")
print("\n before clearing  \n: ",pcb)
print("After Clerring = ",pcb.clear())





