local function split(str, ts)
    if ts == nil then
        return {}
    end
    local t = {};
    i = 1
    for s in string.gmatch(str, "([^" .. ts .. "]+)") do
        t[i] = s
        i = i + 1
    end
    return t
end

local function getCurrentFrame(timeline)
    local timecode = timeline:GetCurrentTimecode()
    local fps = tonumber(timeline:GetSetting('timelineFrameRate'))
    local intFps = {
        [23] = 24,
        [29] = 30,
        [47] = 48,
        [59] = 60,
        [95] = 96,
        [119] = 120,
    }
    if intFps[fps] then
        fps = intFps[fps]
    end
    local isDF = false
    if string.find(timecode, ';') ~= nil then
        isDF = true
        timecode = string.gsub(timecode, ';', ':')
    end
    local t = split(timecode, ':')
    local h = tonumber(t[1])
    local m = tonumber(t[2]) + (h * 60)
    local s = tonumber(t[3]) + (m * 60)
    local f = tonumber(t[4]) + (s * fps)
    local drop_frames = 0
    if isDF then
        local _f = fps / 15
        drop_frames = _f * (m - math.floor(m / 10))
    end
    return f - drop_frames
end
local function getTrackIndexByName(timeline, name)
    local r = nil
    local cnt = timeline:GetTrackCount('video')
    if cnt == 0 then
        return r
    end
    for i = 1, cnt do
        if timeline:GetTrackName('video', i) == name then
            r = i
        end
    end
    return r
end

local function getItemByTrackName_t(timeline, name)
    local r = timeline:GetCurrentVideoItem()
    local index = getTrackIndexByName(timeline, (name .. '_t'))
    if not index then
        print('Track not found: ' .. name .. '_t')
        print('検索トラック名変更: ' .. name)
        index = getTrackIndexByName(timeline, name)
    end
    if not index then
        print('Track not found: ' .. name)
        print('Currentを使います。')
        return r
    end
    local currentFrame = getCurrentFrame(timeline)
    for i, item in ipairs(timeline:GetItemListInTrack('video', index)) do
        if item:GetStart() < currentFrame and item:GetEnd() > currentFrame then
            return item
        end
    end
    print('Item not found')
    print('Currentを使います。')
    return r
end

local function getToolName(st)
    for key, v in pairs(st['Tools']) do
        if (type(v) == 'table') and (v['Inputs'] ~= nil) then
            return key
        end
    end
    return nil
end

local function setJimaku(txt, color, track_name, setting_path)
    local projectManager = resolve:GetProjectManager()
    local project = projectManager:GetCurrentProject()
    if not project then
        print('Projectが見付かりません。')
        return
    end
    local timeline = project:GetCurrentTimeline()
    if not timeline then
        print('Timelineが見付かりません。')
        return
    end
    local textPlus = getItemByTrackName_t(timeline, track_name)
    if not textPlus then
        print('VideoItemが見付かりません。')
        return
    end

    if textPlus:GetFusionCompCount() == 0 then
        print('FusionCompが見付かりません。')
        return
    end

    local comp = textPlus:GetFusionCompByIndex(1)

    local lst = comp:GetToolList(false, 'TextPlus')
    if not lst[1] then
        print('TextPlus Nodeが見付かりません。')
        return
    end

    local tool = lst[1]


    -- setting
    tool.StyledText = txt
    tool.UseFrameFormatSettings = 0
    tool.Width = tonumber(timeline:GetSetting('timelineResolutionWidth'))
    tool.Height = tonumber(timeline:GetSetting('timelineResolutionHeight'))

    local st = tool:SaveSettings()
    local f_st = bmd.readfile(setting_path)
    if not f_st then
        print(setting_path)
        print('settingファイルの読み込みに失敗しました。')
        return
    end
    local name = getToolName(f_st)
    for i, key in pairs({ 'StyledText', 'UseFrameFormatSettings', 'Width', 'Height' }) do
        f_st['Tools'][name]['Inputs'][key] = st['Tools'][tool.Name]['Inputs'][key]
    end

    -- set
    comp:StartUndo('RS Jimaku')
    comp:Lock()
    tool:LoadSettings(f_st)
    comp:Unlock()
    comp:EndUndo(true)

    if color ~= 'None' then
        textPlus:SetClipColor(color)
    end
    print('Dane!(Text+)')
end

setJimaku(
        [[%s]],
        '%s',
        '%s',
        [[%s]]
)