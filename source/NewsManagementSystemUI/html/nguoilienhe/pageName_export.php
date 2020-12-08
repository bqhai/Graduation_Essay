<div class="modal fade" tabindex="-1" role="dialog" id='export-data'>
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button class="close" aria-label="Close" type="button" data-dismiss="modal">
                    <span aria-hidden="true">×</span></button>
                <h4 class="modal-title"><i class='fa fa-download'></i> Export Data</h4>
            </div>


            <div class="modal-body">
                <div class="form-group">
                    <label>File Name</label>
                    <input type='text' name='filename' class='form-control' required value='Report  - 07 Oct 2020' />
                    <div class='help-block'>
                        You can rename the filename according to your whises
                    </div>
                </div>

                <div class="form-group">
                    <label>Max Data</label>
                    <input type='number' name='limit' class='form-control' required value='100' max="100000" min="1" />
                    <div class='help-block'>Minimum 1 and maximum 100,000 rows per export session</div>
                </div>
 
                <div class='form-group'>
                    <label>Columns</label><br />
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='id'>STT</label></div>
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='tenungvien'>Người Liên Hệ</label></div>
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='tuoi'>Chức Danh</label></div>
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='sodienthoai'>Phòng Ban</label></div>
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='diachi'>Điện Thoại</label></div>
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='diachi'>Email</label></div>
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='diachi'>Công Ty</label></div>
                    <div class='checkbox inline'><label><input type='checkbox' checked name='columns[]'
                                value='diachi'>Nhân Viên Chăm Sóc</label></div>
                </div>

                <div class="form-group">
                    <label>Format Export</label>
                    <select name='fileformat' class='form-control'>
                        <option value='pdf'>PDF</option>
                        <option value='xls'>Microsoft Excel (xls)</option>
                        <option value='csv'>CSV</option>
                    </select>
                </div>

                <p><a href='javascript:void(0)' class='toggle_advanced_report'><i class='fa fa-plus-square-o'></i> Show
                        Advanced Export</a></p>

                <div id='advanced_export' style='display: none'>


                    <div class="form-group">
                        <label>Page Size</label>
                        <select class='form-control' name='page_size'>
                            <option value='Letter'>Letter</option>
                            <option value='Legal'>Legal</option>
                            <option value='Ledger'>Ledger</option>
                            <option value='A0'>A0</option>
                            <option value='A1'>A1</option>
                            <option value='A2'>A2</option>
                            <option value='A3'>A3</option>
                            <option value='A4'>A4</option>
                            <option value='A5'>A5</option>
                            <option value='A6'>A6</option>
                            <option value='A7'>A7</option>
                            <option value='A8'>A8</option>

                            <option value='B0'>B0</option>
                            <option value='B1'>B1</option>
                            <option value='B2'>B2</option>
                            <option value='B3'>B3</option>
                            <option value='B4'>B4</option>
                            <option value='B5'>B5</option>
                            <option value='B6'>B6</option>
                            <option value='B7'>B7</option>
                            <option value='B8'>B8</option>
                            <option value='B9'>B9</option>
                            <option value='B10'>B10</option>
                        </select>
                        <div class='help-block'><input type='checkbox' name='default_paper_size' value='1' /> Set As
                            Default Paper Size</div>
                    </div>

                    <div class="form-group">
                        <label>Page Orientation</label>
                        <select class='form-control' name='page_orientation'>
                            <option value='potrait'>Potrait</option>
                            <option value='landscape'>Landscape</option>
                        </select>
                    </div>
                </div>

            </div>
            <div class="modal-footer" align="right">
                <button class="btn btn-default" type="button" data-dismiss="modal">Close</button>
                <button class="btn btn-primary btn-submit" type="submit">Submit</button>
            </div>

        </div>
        <!-- /.modal-content -->
    </div>
</div>