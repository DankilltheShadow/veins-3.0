__author__ = 'Daniel'


#########################mappa colore##############################


##############################################
##plt.hist2d(xcoordheat, ycoordheat, bins=40)
###########################PIE#################
# figure = plt.figure()
# id = 0
# chsum = chstates.iloc[statestime_index[id]].sum()
# onsum = onstates.iloc[statestime_index[id]].sum()
# fnsum = fnstates.iloc[statestime_index[id]].sum()
#
# plt.pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
#
#
# def on_press(event):
#     global id
#     global chsum
#     global onsum
#     global fnsum
#
#     if event.key == u'right' and id < len(statestime_index)-1:
#         event.canvas.figure.clear()
#
#         id += 1
#         chsum += chstates.iloc[statestime_index[id]].sum()
#         onsum += onstates.iloc[statestime_index[id]].sum()
#         fnsum += fnstates.iloc[statestime_index[id]].sum()
#
#         event.canvas.figure.gca().pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
#         event.canvas.draw()
#     else:
#         if event.key == u'left' and id >= 0:
#             event.canvas.figure.clear()
#
#             chsum -= chstates.iloc[statestime_index[id]].sum()
#             onsum -= onstates.iloc[statestime_index[id]].sum()
#             fnsum -= fnstates.iloc[statestime_index[id]].sum()
#             id -= 1
#
#             event.canvas.figure.gca().pie([fnsum, onsum, chsum], labels=['FN', 'ON', 'CH'], autopct='%1.1f%%', shadow=False, startangle=90)
#             event.canvas.draw()
#
# figure.canvas.mpl_connect('key_press_event', on_press)
#plt.show()
