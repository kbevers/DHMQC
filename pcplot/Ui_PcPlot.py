# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PcPlot.ui'
#
# Created: Thu Jul 03 12:19:35 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(769, 687)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.cb_indexlayers = QtGui.QComboBox(self.groupBox_4)
        self.cb_indexlayers.setObjectName(_fromUtf8("cb_indexlayers"))
        self.horizontalLayout_6.addWidget(self.cb_indexlayers)
        self.bt_refresh_index_layer = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_refresh_index_layer.sizePolicy().hasHeightForWidth())
        self.bt_refresh_index_layer.setSizePolicy(sizePolicy)
        self.bt_refresh_index_layer.setObjectName(_fromUtf8("bt_refresh_index_layer"))
        self.horizontalLayout_6.addWidget(self.bt_refresh_index_layer)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.txt_grid_path = QtGui.QLineEdit(self.groupBox_4)
        self.txt_grid_path.setObjectName(_fromUtf8("txt_grid_path"))
        self.horizontalLayout_9.addWidget(self.txt_grid_path)
        self.bt_browse_griddir = QtGui.QPushButton(self.groupBox_4)
        self.bt_browse_griddir.setObjectName(_fromUtf8("bt_browse_griddir"))
        self.horizontalLayout_9.addWidget(self.bt_browse_griddir)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.formLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.bt_grid_tile = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_grid_tile.sizePolicy().hasHeightForWidth())
        self.bt_grid_tile.setSizePolicy(sizePolicy)
        self.bt_grid_tile.setObjectName(_fromUtf8("bt_grid_tile"))
        self.horizontalLayout_7.addWidget(self.bt_grid_tile)
        self.bt_hillshade_tile = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_hillshade_tile.sizePolicy().hasHeightForWidth())
        self.bt_hillshade_tile.setSizePolicy(sizePolicy)
        self.bt_hillshade_tile.setObjectName(_fromUtf8("bt_hillshade_tile"))
        self.horizontalLayout_7.addWidget(self.bt_hillshade_tile)
        self.bt_density_tile = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_density_tile.sizePolicy().hasHeightForWidth())
        self.bt_density_tile.setSizePolicy(sizePolicy)
        self.bt_density_tile.setObjectName(_fromUtf8("bt_density_tile"))
        self.horizontalLayout_7.addWidget(self.bt_density_tile)
        self.bt_class_tile = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_class_tile.sizePolicy().hasHeightForWidth())
        self.bt_class_tile.setSizePolicy(sizePolicy)
        self.bt_class_tile.setObjectName(_fromUtf8("bt_class_tile"))
        self.horizontalLayout_7.addWidget(self.bt_class_tile)
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.spb_cellsize = QtGui.QDoubleSpinBox(self.groupBox_4)
        self.spb_cellsize.setMinimum(0.2)
        self.spb_cellsize.setMaximum(200.0)
        self.spb_cellsize.setProperty("value", 1.0)
        self.spb_cellsize.setObjectName(_fromUtf8("spb_cellsize"))
        self.horizontalLayout_7.addWidget(self.spb_cellsize)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_5)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txt_las_path = QtGui.QLineEdit(self.groupBox_5)
        self.txt_las_path.setObjectName(_fromUtf8("txt_las_path"))
        self.horizontalLayout.addWidget(self.txt_las_path)
        self.bt_browse_lasdir = QtGui.QPushButton(self.groupBox_5)
        self.bt_browse_lasdir.setObjectName(_fromUtf8("bt_browse_lasdir"))
        self.horizontalLayout.addWidget(self.bt_browse_lasdir)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.bt_build_index = QtGui.QPushButton(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_build_index.sizePolicy().hasHeightForWidth())
        self.bt_build_index.setSizePolicy(sizePolicy)
        self.bt_build_index.setObjectName(_fromUtf8("bt_build_index"))
        self.horizontalLayout_8.addWidget(self.bt_build_index)
        self.chb_walk_folders = QtGui.QCheckBox(self.groupBox_5)
        self.chb_walk_folders.setChecked(True)
        self.chb_walk_folders.setObjectName(_fromUtf8("chb_walk_folders"))
        self.horizontalLayout_8.addWidget(self.chb_walk_folders)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 10, 1, 1)
        self.spb_max = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.spb_max.setEnabled(False)
        self.spb_max.setMaximum(300.0)
        self.spb_max.setObjectName(_fromUtf8("spb_max"))
        self.gridLayout.addWidget(self.spb_max, 0, 7, 1, 1)
        self.spb_min = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.spb_min.setEnabled(False)
        self.spb_min.setMaximum(300.0)
        self.spb_min.setSingleStep(1.0)
        self.spb_min.setObjectName(_fromUtf8("spb_min"))
        self.gridLayout.addWidget(self.spb_min, 0, 5, 1, 1)
        self.chb_restrict = QtGui.QCheckBox(self.groupBox_2)
        self.chb_restrict.setObjectName(_fromUtf8("chb_restrict"))
        self.gridLayout.addWidget(self.chb_restrict, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.chb_strip_color = QtGui.QCheckBox(self.groupBox_2)
        self.chb_strip_color.setObjectName(_fromUtf8("chb_strip_color"))
        self.gridLayout.addWidget(self.chb_strip_color, 0, 8, 1, 1)
        self.chb_axis_equal = QtGui.QCheckBox(self.groupBox_2)
        self.chb_axis_equal.setChecked(True)
        self.chb_axis_equal.setObjectName(_fromUtf8("chb_axis_equal"))
        self.gridLayout.addWidget(self.chb_axis_equal, 0, 9, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.bt_z_interval_poly = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_z_interval_poly.sizePolicy().hasHeightForWidth())
        self.bt_z_interval_poly.setSizePolicy(sizePolicy)
        self.bt_z_interval_poly.setObjectName(_fromUtf8("bt_z_interval_poly"))
        self.horizontalLayout_4.addWidget(self.bt_z_interval_poly)
        self.bt_plot2d = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_plot2d.sizePolicy().hasHeightForWidth())
        self.bt_plot2d.setSizePolicy(sizePolicy)
        self.bt_plot2d.setObjectName(_fromUtf8("bt_plot2d"))
        self.horizontalLayout_4.addWidget(self.bt_plot2d)
        self.bt_plot3d = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_plot3d.sizePolicy().hasHeightForWidth())
        self.bt_plot3d.setSizePolicy(sizePolicy)
        self.bt_plot3d.setObjectName(_fromUtf8("bt_plot3d"))
        self.horizontalLayout_4.addWidget(self.bt_plot3d)
        self.bt_dump_csv = QtGui.QPushButton(self.groupBox)
        self.bt_dump_csv.setObjectName(_fromUtf8("bt_dump_csv"))
        self.horizontalLayout_4.addWidget(self.bt_dump_csv)
        self.chb_add_csv = QtGui.QCheckBox(self.groupBox)
        self.chb_add_csv.setObjectName(_fromUtf8("chb_add_csv"))
        self.horizontalLayout_4.addWidget(self.chb_add_csv)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cb_polygonlayers = QtGui.QComboBox(self.groupBox)
        self.cb_polygonlayers.setEditable(False)
        self.cb_polygonlayers.setObjectName(_fromUtf8("cb_polygonlayers"))
        self.horizontalLayout_2.addWidget(self.cb_polygonlayers)
        self.bt_refresh_polygons = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_refresh_polygons.sizePolicy().hasHeightForWidth())
        self.bt_refresh_polygons.setSizePolicy(sizePolicy)
        self.bt_refresh_polygons.setObjectName(_fromUtf8("bt_refresh_polygons"))
        self.horizontalLayout_2.addWidget(self.bt_refresh_polygons)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.bt_add_polygon_layer = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_add_polygon_layer.sizePolicy().hasHeightForWidth())
        self.bt_add_polygon_layer.setSizePolicy(sizePolicy)
        self.bt_add_polygon_layer.setObjectName(_fromUtf8("bt_add_polygon_layer"))
        self.verticalLayout_3.addWidget(self.bt_add_polygon_layer)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.bt_z_interval_line = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_z_interval_line.sizePolicy().hasHeightForWidth())
        self.bt_z_interval_line.setSizePolicy(sizePolicy)
        self.bt_z_interval_line.setObjectName(_fromUtf8("bt_z_interval_line"))
        self.horizontalLayout_5.addWidget(self.bt_z_interval_line)
        self.bt_plot_vertical = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_plot_vertical.sizePolicy().hasHeightForWidth())
        self.bt_plot_vertical.setSizePolicy(sizePolicy)
        self.bt_plot_vertical.setObjectName(_fromUtf8("bt_plot_vertical"))
        self.horizontalLayout_5.addWidget(self.bt_plot_vertical)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.spb_buffer_dist = QtGui.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spb_buffer_dist.sizePolicy().hasHeightForWidth())
        self.spb_buffer_dist.setSizePolicy(sizePolicy)
        self.spb_buffer_dist.setMinimum(0.2)
        self.spb_buffer_dist.setObjectName(_fromUtf8("spb_buffer_dist"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.spb_buffer_dist)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cb_linelayers = QtGui.QComboBox(self.groupBox_3)
        self.cb_linelayers.setObjectName(_fromUtf8("cb_linelayers"))
        self.horizontalLayout_3.addWidget(self.cb_linelayers)
        self.bt_refresh_lines = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_refresh_lines.sizePolicy().hasHeightForWidth())
        self.bt_refresh_lines.setSizePolicy(sizePolicy)
        self.bt_refresh_lines.setObjectName(_fromUtf8("bt_refresh_lines"))
        self.horizontalLayout_3.addWidget(self.bt_refresh_lines)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.bt_add_line_layer = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_add_line_layer.sizePolicy().hasHeightForWidth())
        self.bt_add_line_layer.setSizePolicy(sizePolicy)
        self.bt_add_line_layer.setObjectName(_fromUtf8("bt_add_line_layer"))
        self.verticalLayout_2.addWidget(self.bt_add_line_layer)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.txt_log = QtGui.QTextEdit(Dialog)
        self.txt_log.setObjectName(_fromUtf8("txt_log"))
        self.verticalLayout.addWidget(self.txt_log)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.chb_restrict, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spb_max.setEnabled)
        QtCore.QObject.connect(self.chb_restrict, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spb_min.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PcPlot plugin", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Las file index (polygons)", None))
        self.bt_refresh_index_layer.setText(_translate("Dialog", "Refresh", None))
        self.label_7.setText(_translate("Dialog", "Grid output dir:", None))
        self.bt_browse_griddir.setText(_translate("Dialog", "Browse", None))
        self.bt_grid_tile.setText(_translate("Dialog", "grid tile", None))
        self.bt_hillshade_tile.setText(_translate("Dialog", "hillshade tile", None))
        self.bt_density_tile.setText(_translate("Dialog", "density grid of tile", None))
        self.bt_class_tile.setText(_translate("Dialog", "class grid of tile", None))
        self.label_8.setText(_translate("Dialog", "Cellsize:", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Build las file index", None))
        self.label.setText(_translate("Dialog", "Path to las tiles:", None))
        self.bt_browse_lasdir.setText(_translate("Dialog", "Browse", None))
        self.bt_build_index.setText(_translate("Dialog", "Build new index", None))
        self.chb_walk_folders.setText(_translate("Dialog", "Walk into sub folders", None))
        self.groupBox_2.setTitle(_translate("Dialog", " Plot options", None))
        self.chb_restrict.setText(_translate("Dialog", "Restrict to z-inteval", None))
        self.label_2.setText(_translate("Dialog", "from:", None))
        self.label_3.setText(_translate("Dialog", "to:", None))
        self.chb_strip_color.setText(_translate("Dialog", "Color by strip id", None))
        self.chb_axis_equal.setText(_translate("Dialog", "Axis \"equal\" (only applies to vertical plot)", None))
        self.groupBox.setTitle(_translate("Dialog", "Plot in polygon", None))
        self.bt_z_interval_poly.setText(_translate("Dialog", "Get z-interval", None))
        self.bt_plot2d.setText(_translate("Dialog", "2d plot", None))
        self.bt_plot3d.setText(_translate("Dialog", "3d plot", None))
        self.bt_dump_csv.setText(_translate("Dialog", "Dump csv", None))
        self.chb_add_csv.setText(_translate("Dialog", "Add csv layer to canvas - its gonna be slow!", None))
        self.label_5.setText(_translate("Dialog", "Selected polygon layer", None))
        self.bt_refresh_polygons.setText(_translate("Dialog", "Refresh", None))
        self.bt_add_polygon_layer.setText(_translate("Dialog", "Add temporary polygon layer", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Plot vertical section", None))
        self.bt_z_interval_line.setText(_translate("Dialog", "Get z-interval", None))
        self.bt_plot_vertical.setText(_translate("Dialog", "Vertical plot", None))
        self.label_4.setText(_translate("Dialog", "Buffer distance:", None))
        self.label_6.setText(_translate("Dialog", "Selected line layer", None))
        self.bt_refresh_lines.setText(_translate("Dialog", "Refresh", None))
        self.bt_add_line_layer.setText(_translate("Dialog", "Add temporary line layer", None))
